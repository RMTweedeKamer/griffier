# Defaults
import sentry_sdk
import json
import os

# Discord
import discord
from discord.ext import commands

# Derde partij
import aiohttp

# Laad alle cogs
from utils.error_handler import CommandErrorHandler
from utils.utilities import Utils
from cogs.customchannels import CustomChannels
# from cogs.autormtkapi import AutoRMTKAPI
from cogs.announcements import Announcements
from cogs.greeter import Greeter
from cogs.starboard import Starboard
from cogs.pinner import Pinner
from cogs.eightball import Eightball
from cogs.zoltar import Zoltar
from cogs.mute import Mute
from cogs.sleepnet import Sleepnet
import sentry_sdk


class PleaseIgnoreMyException(Exception):
    pass

class Griffier(commands.Cog):
    def __init__(self, bot, host_id, utils):
        self.bot = bot
        self.host_id = host_id
        self.utils = utils

        if 'jail' not in self.utils.settings:
            self.utils.settings['jail'] = {}

        self.utils.save_settings()

    @commands.Cog.listener()
    async def on_command_error(self, context, error):
        if isinstance(error, commands.UserInputError):
            await context.send('```{}```'.format(error))
            await self.utils.send_cmd_help(context)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ingelogd als')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0'.format(self.bot.user.id))
        print('-' * 20)

    @commands.command(name='ping')
    async def ping(self, context):
        '''Stuur een ping-pong balletje'''
        if self.utils.jail_check(context.command, context.channel.id):
            await context.message.add_reaction('\U0001F3D3')

    @commands.command(name='jail')
    @commands.is_owner()
    async def jail(self, context, command: str):
        '''Een commando mag niet in dit kanaal worden gebruikt.'''
        channel = context.channel.id

        if command not in self.utils.settings['jail']:
            self.utils.settings['jail'][command] = []

        if channel not in self.utils.settings['jail'][command]:
            self.utils.settings['jail'][command].append(channel)

        self.utils.save_settings()

        await context.message.add_reaction('\U0001F44D')

    @commands.command(name='unjail')
    @commands.is_owner()
    async def unjail(self, context, command: str):
        '''Een commando mag weer in dit kanaal worden gebruikt.'''
        channel = context.channel.id

        if command in self.utils.settings['jail']:
            if channel in self.utils.settings['jail'][command]:
                self.utils.settings['jail'][command].remove(channel)

                self.utils.save_settings()

        await context.message.add_reaction('\U0001F44D')

    @commands.command(name='afsluiten', aliases=['shutdown'])
    @commands.is_owner()
    async def shutdown_bot(self, context):
        '''Sluit Griffier af'''
        await context.send('Deze zitting is gesloten.')
        await bot.logout()

    @commands.command(name='throw_error')
    async def throw_error(self, context):
        raise PleaseIgnoreMyException()

    @commands.group(name='update')
    @commands.is_owner()
    async def update(self, context):
        '''De bot bijwerken'''

    @update.command(name='afbeelding', aliases=['avatar'])
    async def avatar(self, context, url: str):
        '''Verander de afbeelding van Griffier'''
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                data = await r.read()

        try:
            await context.bot.user.edit(avatar=data)
        except discord.HTTPException:
            await context.send('Het veranderen van de afbeelding is mislukt. Je kunt de afbeelding '
                               'slechts 2 keer per uur veranderen.')
        except discord.InvalidArgument:
            await context.send('Alleen JPG of PNG formaat.')
        else:
            await context.message.add_reaction('\U0001F44D')

    @update.command(name='gebruikersnaam', aliases=['username'])
    async def _username(self, context, *, username: str):
        '''Verander de gebruikersnaam van Griffier'''
        try:
            await self.bot.user.edit(name=username)
        except discord.HTTPException:
            await context.send('Kon de gebruikersnaam niet veranderen. Je kunt maar '
                               '2 keer per uur de gebruikersnaam veranderen.')
        else:
            await context.message.add_reaction('\U0001F44D')


if not os.path.exists('data/settings.json'):
    with open('data/settings.json', encoding='utf-8', mode='w') as f:
        f.write(json.dumps({}))
        f.close()

if not os.path.exists('config.json'):
    with open('config.json', encoding='utf-8', mode='w') as f:
        token = input('token> ')
        reddit_client_id = input('reddit client id> ')
        reddit_client_secret = input('reddit client secret> ')
        host_id = input('member id of hoster> ')
        prefix = input('prefix> ')
        config = json.dumps({'token': token, 'reddit_client_secret': reddit_client_secret, 'reddit_client_id': reddit_client_id, 'host_id': host_id, 'prefix': prefix})
        f.write(config)
        f.close()

with open('config.json', encoding='utf-8', mode='r') as f:
        config = json.load(f)

token = config['token']
reddit_client_id = config['reddit_client_id']
reddit_client_secret = config['reddit_client_secret']
host_id = config['host_id']
prefix = config['prefix']
sentry = config['sentry']
environment = config['environment']

bot = commands.Bot(command_prefix=prefix,
                   activity=discord.Activity(name='NPO Polertiek',
                                             type=discord.ActivityType.watching))

# Data manager en zo...
utils = Utils(bot)

sentry_sdk.init(dsn=sentry, environment=environment)

# De bot
bot.add_cog(Griffier(bot, host_id, utils))
bot.add_cog(CommandErrorHandler(bot))

# Laad cogs
bot.add_cog(CustomChannels(bot, utils, prefix))
bot.add_cog(Announcements(bot, utils, reddit_client_id, reddit_client_secret))
bot.add_cog(Greeter(bot, utils))
bot.add_cog(Starboard(bot, utils))
bot.add_cog(Pinner(bot, utils))
bot.add_cog(Eightball(bot, utils))
bot.add_cog(Zoltar(bot, utils))
bot.add_cog(Mute(bot, utils))
bot.add_cog(Sleepnet(bot, utils))

bot.run(token)
