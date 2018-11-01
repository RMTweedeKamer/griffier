from discord.ext import commands
from random import choice


class Zoltar:
    def __init__(self, bot, utils):
        self.bot = bot
        self.utils = utils
        self.antwoorden = ["Today it's up to you to create the peacefulness you long for.", 'A friend asks only for your time not your money.', 'If you refuse to accept anything but the best, you very often get it.', 'A smile is your passport into the hearts of others.', 'A good way to keep healthy is to eat more Chinese food.', 'Your high-minded principles spell success.', 'Hard work pays off in the future, laziness pays off now.', 'Change can hurt, but it leads a path to something better.', 'Enjoy the good luck a companion brings you.', 'People are naturally attracted to you.', 'Hidden in a valley beside an open stream- This will be the type of place where you will find your dream.', 'A chance meeting opens new doors to success and friendship.', 'You learn from your mistakes... You will learn a lot today.', "If you have something good in your life, don't let it go!", "What ever you're goal is in life, embrace it visualize it, and for it will be yours.", 'Your shoes will make you happy today.', 'You cannot love life until you live the life you love.', 'Be on the lookout for coming events; They cast their shadows beforehand.', 'Land is always on the mind of a flying bird.', 'The man or woman you desire feels the same about you.', 'Meeting adversity well is the source of your strength.', 'A dream you have will come true.', 'Our deeds determine us, as much as we determine our deeds.', "Never give up. You're not a failure if you don't give up.", 'You will become great if you believe in yourself.', 'There is no greater pleasure than seeing your loved ones prosper.', 'You will marry your lover.', 'A very attractive person has a message for you.', 'You already know the answer to the questions lingering inside your head.', 'It is now, and in this world, that we must live.', 'You must try, or hate yourself for not trying.', 'You can make your own happiness.', 'The greatest risk is not taking one.', 'The love of your life is stepping into your planet this summer.', 'Love can last a lifetime, if you want it to.', 'Adversity is the parent of virtue.', 'Serious trouble will bypass you.', 'A short stranger will soon enter your life with blessings to share.', 'Now is the time to try something new.', 'Wealth awaits you very soon.', 'If you feel you are right, stand firmly by your convictions.', 'If winter comes, can spring be far behind?', 'Keep your eye out for someone special.', 'You are very talented in many ways.', 'A stranger, is a friend you have not spoken to yet.', 'A new voyage will fill your life with untold memories.', 'You will travel to many exotic places in your lifetime.', 'Your ability for accomplishment will follow with success.', 'Nothing astonishes men so much as common sense and plain dealing.', 'Its amazing how much good you can do if you dont care who gets the credit.', 'Everyone agrees. You are the best.', 'LIFE CONSIST NOT IN HOLDING GOOD CARDS, BUT IN PLAYING THOSE YOU HOLD WELL.', "Jealousy doesn't open doors, it closes them!", "It's better to be alone sometimes.", 'When fear hurts you, conquer it and defeat it!', 'Let the deeds speak.', 'You will be called in to fulfill a position of high honor and responsibility.', 'The man on the top of the mountain did not fall there.', 'You will conquer obstacles to achieve success.', 'Joys are often the shadows, cast by sorrows.', 'Fortune favors the brave.', 'An upward movement initiated in time can counteract fate.', 'A journey of a thousand miles begins with a single step.', 'Sometimes you just need to lay on the floor.', 'Never give up. Always find a reason to keep trying.', 'If you have something worth fighting for, then fight for it.', 'Stop wishing. Start doing.', 'Accept your past without regrets. Handle your present with confidence. Face your future without fear.', 'Stay true to those who would do the same for you.', 'Ask yourself if what you are doing today is getting you closer to where you want to be tomorrow.', 'Happiness is an activity.', 'Help is always needed but not always appreciated. Stay true to your heart and help those in need weather they appreciate it or not.', 'Hone your competitive instincts.', "Finish your work on hand don't be greedy.", 'For success today, look first to yourself.', 'Your fortune is as sweet as a cookie.', 'Integrity is the essence of everything successful.', "If you're happy, you're successful.", 'You will always be surrounded by true friends', 'Believing that you are beautiful will make you appear beautiful to others around you.', 'Happinees comes from a good life.', 'Before trying to please others think of what makes you happy.', 'When hungry, order more Chinese food.', 'Your golden opportunity is coming shortly.', 'For hate is never conquered by hate. Hate is conquered by love .', 'You will make many changes before settling down happily.', 'A man is born to live and not prepare to live.', 'You cannot become rich except by enriching others.', "Don't pursue happiness - create it.", 'You will be successful in love.', "All your fingers can't be of the same length.", 'Wise sayings often fall on barren ground, but a kind word is never thrown away.', 'A lifetime of happiness is in store for you.', 'It is very possible that you will achieve greatness in your lifetime.', 'Be tactful; overlook your own opportunity.', 'You are the controller of your destiny.', 'Everything happens for a reson.', 'How can you have a beutiful ending without making beautiful mistakes.', 'You can open doors with your charm and patience.', 'Welcome the change coming into your life.', 'There will be a happy romance for you shortly.', 'Your fondest dream will come true within this year.', 'You have a deep interest in all that is artistic.', 'Your emotional nature is strong and sensitive.', 'A letter of great importance may reach you any day now.', 'Good health will be yours for a long time.', 'You will become better acquainted with a coworker.', 'To be old and wise, you must first be young and stupid.', 'Failure is only the opportunity to begin again more intelligently.', 'Integrity is doing the right thing, even if nobody is watching.', 'Conquer your fears or they will conquer you.', 'You are a lover of words; One day you will write a book.', 'In this life it is not what we take up, but what we give up, that makes us rich.', 'Fear can keep us up all night long, but faith makes one fine pillow.', 'Seek out the significance of your problem at this time. Try to understand.', "Never upset the driver of the car you're in; they're the master of your destiny until you get home.", 'He who slithers among the ground is not always a foe.', 'You learn from your mistakes, you will learn a lot today.', 'You only need look to your own reflection for inspiration. Because you are Beautiful!', 'You are not judged by your efforts you put in; you are judged on your performance.', 'Rivers need springs.', 'Good news from afar may bring you a welcome visitor.', 'When all else seems to fail, smile for today and just love someone.', 'Patience is a virtue, unless its against a brick wall.', 'When you look down, all you see is dirt, so keep looking up.', 'If you are afraid to shake the dice, you will never throw a six.', 'Even if the person who appears most wrong, is also quite often right.', 'A single conversation with a wise man is better than ten years of study.', 'Happiness is often a rebound from hard work.', "The world may be your oyster, but that doesn't mean you'll get it's pearl.", 'Your life will be filled with magical moments.', "You're true love will show himself to you under the moonlight.", 'Do not follow where the path may lead. Go where there is no path...and leave a trail', "Do not fear what you don't know", 'The object of your desire comes closer.', 'You have a flair for adding a fanciful dimension to any story.', 'If you wish to know the mind of a man, listen to his words', 'The most useless energy is trying to change what and who God so carefully created.', 'Do not be covered in sadness or be fooled in happiness they both must exist', 'You will have unexpected great good luck.', 'You will have a pleasant surprise', 'All progress occurs because people dare to be different.', 'Your ability for accomplishment will be followed by success.', 'The world is always ready to receive talent with open arms.', 'Things may come to those who wait, but only the things left by those who hustle.', "We can't help everyone. But everyone can help someone.", 'Every day is a new day. But tomorrow is never promised.', "Express yourself: Don't hold back!", 'It is not necessary to show others you have change; the change will be obvious.', 'You have a deep appreciation of the arts and music.', 'If your desires are not extravagant, they will be rewarded.', "You try hard, never to fail. You don't, never to win.", "Never give up on someone that you don't go a day without thinking about.", 'It never pays to kick a skunk.', 'In case of fire, keep calm, pay bill and run.', 'Next full moon brings an enchanting evening.', 'Not all closed eye is sleeping nor open eye is seeing.', 'Impossible is a word only to be found in the dictionary of fools.', 'You will soon witness a miracle.', 'The time is alway right to do what is right.', 'Love is as necessary to human beings as food and shelter.', 'You will make heads turn.', "You are extremely loved. Don't worry :)", 'If you are never patient, you will never get anything done. If you believe you can do it, you will be rewarded with success.', 'You will soon embark on a business venture.', 'You believe in the goodness of man kind.', 'You will have a long and wealthy life.', 'You will take a pleasant journey to a place far away.', 'You are a person of culture.', 'Keep it simple. The more you say, the less people remember.', "Life is like a dogsled team. If you ain't the lead dog, the scenery never changes.", 'Prosperity makes friends and adversity tries them.', 'Nothing seems impossible to you.', 'Patience is bitter, but its fruit is sweet.', 'The only certainty is that nothing is certain.', 'Success is the sum of my unique visions realized by the sweat of perseverance.', 'When you expect your opponent to yield, you also should avoid hurting him.', 'Human evolution: "wider freeway" but narrower viewpoints.', 'Intelligence is the door to freedom and alert attention is the mother of intelligence.', 'Back away from individuals who are impulsive.', 'Enjoyed the meal? Buy one to go too.', 'You believe in the goodness of mankind.', 'A big fortune will descend upon you this year.', 'Now these three remain, faith, hope, and love. The greatest of these is love.', 'For success today look first to yourself.', 'Determination is the wake-up call to the human will.', 'There are no limitations to the mind except those we aknowledge.', 'A merry heart does good like a medicine.', 'Whenever possible, keep it simple.', 'Your dearest wish will come true.', 'Poverty is no disgrace.', 'If you don’t do it excellently, don’t do it at all.', 'You have an unusual equipment for success, use it properly.', 'Emotion is energy in motion.', 'You will soon be honored by someone you respect.', 'Punctuality is the politeness of kings and the duty of gentle people everywhere.', 'Your happiness is intertwined with your outlook on life.', 'Elegant surroundings will soon be yours.', 'If you feel you are right, stand firmly by your convictions.', 'Your smile brings happiness to everyone you meet.', 'If your desires are not extravagant, they will be rewarded.', "You try hard, never to fail. You don't, never to win.", "Never give up on someone that you don't go a day without thinking about.", 'It never pays to kick a skunk.', 'In case of fire, keep calm, pay bill and run.', 'Next full moon brings an enchanting evening.', 'Not all closed eye is sleeping nor open eye is seeing.', 'Impossible is a word only to be found in the dictionary of fools.', 'You will soon witness a miracle.', 'The time is alway right to do what is right.', 'Love is as necessary to human beings as food and shelter.', 'You will make heads turn.', "You are extremely loved. Don't worry :)", 'If you are never patient, you will never get anything done. If you believe you can do it, you will be rewarded with success.', 'You will soon embark on a business venture.', 'You believe in the goodness of man kind.', 'You will have a long and wealthy life.', 'You will take a pleasant journey to a place far away.', 'You are a person of culture.', 'Keep it simple. The more you say, the less people remember.', "Life is like a dogsled team. If you ain't the lead dog, the scenery never changes.", 'Prosperity makes friends and adversity tries them.', 'Nothing seems impossible to you.', 'Patience is bitter, but its fruit is sweet.', 'The only certainty is that nothing is certain.', 'Success is the sum of my unique visions realized by the sweat of perseverance.', 'When you expect your opponent to yield, you also should avoid hurting him.', 'Human evolution: "wider freeway" but narrower viewpoints.', 'Intelligence is the door to freedom and alert attention is the mother of intelligence.', 'Back away from individuals who are impulsive.', 'Enjoyed the meal? Buy one to go too.', 'You believe in the goodness of mankind.', 'A big fortune will descend upon you this year.', 'Now these three remain, faith, hope, and love. The greatest of these is love.', 'For success today look first to yourself.', 'Determination is the wake-up call to the human will.', 'There are no limitations to the mind except those we aknowledge.', 'A merry heart does good like a medicine.', 'Whenever possible, keep it simple.', 'Your dearest wish will come true.', 'Poverty is no disgrace.', 'If you don’t do it excellently, don’t do it at all.', 'You have an unusual equipment for success, use it properly.', 'Emotion is energy in motion.', 'You will soon be honored by someone you respect.', 'Punctuality is the politeness of kings and the duty of gentle people everywhere.', 'Your happiness is intertwined with your outlook on life.', 'Elegant surroundings will soon be yours.', 'If you feel you are right, stand firmly by your convictions.', 'Your smile brings happiness to everyone you meet.', 'Instead of worrying and agonizing, move ahead constructively.', 'Do you believe? Endurance and persistence will be rewarded.', 'A new business venture is on the horizon.', 'Never underestimate the power of the human touch.', 'Hold on to the past but eventually, let the times go and keep the memories into the present.', 'Truth is an unpopular subject. Because it is unquestionably correct.', 'The most important thing in communication is to hear what isn’t being said.', 'You are broad minded and socially active.', 'Your dearest dream is coming true. God looks after you especially.', 'You will recieve some high prize or award.', 'Your present question marks are going to succeed.', 'You have a fine capacity for the enjoyment of life.', 'You will live long and enjoy life.', 'An admirer is concealing his/her affection for you.', 'A wish is what makes life happen when you dream of rose petals.', 'Love can turn cottage into a golden palace.', 'Lend your money and lose your freind.', 'You will kiss your crush ohhh lalahh', 'You will be rewarded for being a good listener in the next week.', 'If you never give up on love, It will never give up on you.', 'Unleash your life force.', 'Your wish will come true.', 'There is a prospect of a thrilling time ahead for you.', 'No distance is too far, if two hearts are tied together.', 'Land is always in the mind of the flying birds.', 'Try? No! Do or do not, there is no try.', 'Do not worry, you will have great peace.', "It's about time you asked that special someone on a date.", 'You create your own stage ... the audience is waiting.', 'It is never too late. Just as it is never too early.', 'Discover the power within yourself.', 'Good things take time.', 'Stop thinking about the road not taken and pave over the one you did.', 'Put your unhappiness aside. Life is beautiful, be happy.', 'You can still love what you can not have in life.', 'Make a wise choice everyday.', 'Circumstance does not make the man; it reveals him to himself.', 'The man who waits till tomorrow, misses the opportunities of today.', 'Life does not get better by chance. It gets better by change.', 'If you never expect anything you can never be disappointed.', 'People in your surroundings will be more cooperative than usual.', 'True wisdom is found in happiness.', 'Ones always regrets what could have done. Remember for next time.', 'Follow your bliss and the Universe will open doors where there were once only walls.', 'Find a peaceful place where you can make plans for the future.', "All the water in the world can't sink a ship unless it gets inside.", 'The earth is a school learn in it.', 'In music, one must think with his heart and feel with his brain.', 'If you speak honestly, everyone will listen.', 'Ganerosity will repay itself sooner than you imagine.', 'good things take time', 'Do what is right, not what you should.', 'To effect the quality of the day is no small achievement.', 'Simplicity and clearity should be the theme in your dress.', 'Virtuous find joy while Wrongdoers find grieve in their actions.', 'Not all closed eye is sleeping, nor open eye is seeing.', 'Bread today is better than cake tomorrow.', 'In evrything there is a piece of truth.But a piece.', 'A feeling is an idea with roots.', 'Man is born to live and not prepare to live.', "It's all right to have butterflies in your stomach. Just get them to fly in formation.", 'If you don t give something, you will not get anything', 'The harder you try to not be like your parents, the more likely you will become them', 'Someday everything will all make perfect sense', 'you will think for yourself when you stop letting others think for you.', "Everything will be ok. Don't obsess. Time will prove you right, you must stay where you are.", "Let's finish this up now, someone is waiting for you on that.", 'The finest men like the finest steels have been tempered in the hottest furnace.', 'A dream you have will come true.', 'The worst of friends may become the best of enemies, but you will always find yourself hanging on.', 'I think, you ate your fortune while you were eating your cookie.', 'If u love someone keep fighting for them.', 'Do what you want, when you want, and you will be rewarded', 'Let your fantasies unwind...', 'The cooler you think you are the dumber you look', 'Expect great things and great things will come', 'The Wheel of Good Fortune is finally turning in your direction!', "Don't lead if you won't lead.", 'You will always be successful in your professional career', 'Share your hapiness with others today.', "It's up to you to clearify.", 'Your future will be happy and productive.', 'Seize every second of your life and savor it.', "Those who walk in other's tracks leave no footprints.", 'Failure is the mother of all success.', 'Difficulty at the beginning useually means ease at the end.', 'Do not seek so much to find the answer as much as to understand the question better.', 'Your way of doing what other people do their way is what makes you special.', 'A beautiful, smart, and loving person will be coming into your life.', 'Friendship is an ocean that you cannot see bottom.', 'Your life does not get better by chance, it gets better by change.', 'Our duty,as men and women,is to proceed as if limits to our ability did not exist.', "A pleasant expeience is ahead:don't pass it by.", 'Our perception and attitude toward any situation will determine the outcome', 'They say you are stubborn; you call it persistence.', 'Two small jumps are sometimes better than one big leap.', 'A new wardrobe brings great joy and change to your life.', 'The cure for grief is motion.', "It's a good thing that life is not as serious as it seems to the waiter", 'I hear and I forget. I see and I remember. I do and I understand.', 'I have a dream....Time to go to bed.', 'Ideas you believe are absurd ultimately lead to success!', 'A human being is a deciding being.', 'Today is an ideal time to water your parsonal garden.', 'Some men dream of fortunes, others dream of cookies.', 'Things are never quite the way they seem.', 'the project on your mind will soon gain momentum', 'YOUR FAILURES WILL LEAD YOU TO YOUR SUCCESS.', 'IN ORDER TO GET THE RAINBOW, YOU MUST ENDURE THE RAIN.', 'Beauty is simply beauty. originality is magical.', 'Your dream will come true when you least expect it.', 'Let not your hand be stretched out to receive and shut when you should repay.', "Don't worry, half the people you know are below average.", 'Vision is the art of seeing what is invisible to others.', "You don't need talent to gain experience.", 'A focused mind is one of the most powerful forces in the universe.', 'Today you shed your last tear. Tomorrow fortune knocks at your door.', "Be patient! The Great Wall didn't got build in one day.", "Think you can. Think you can't. Either way, you'll be right.", 'Wisdom is on her way to you.', 'Digital circuits are made from analog parts.', 'If you eat a box of fortune cookies, anything is possible.', 'The best is yet to come.', "I'm with you.", 'Be direct,usually one can accomplish more that way.', 'A single kind work will keep one warm for years.', 'Ask a friend to join you on your next voyage.', 'In God we trust.', 'Love is free. Lust will cost you everything you have.', 'Stop searching forever, happiness is just next to you.', "You don't need the answers to all of life's questions. Just ask your father what to do.", 'Jealousy is a useless emotion.', 'You are not a ghost.', 'There is someone rather annoying in your life that you need to listen to.', 'You will plant the smallest seed and it will become the greatest and most mighty tree in the world.', "The dream you've been dreaming all your life isn't worth it. Find a new dream, and once you're sure you've found it, fight for it.", 'See if you can learn anything from the children.', "It's Never Too Late For Good Things To Happen!", 'A clear conscience is usually the sign of a bad memory.', 'Aim high, time flies.', 'One is not sleeping, does not mean they are awake.', "A great pleasure in life is doing what others say you can't.", "Isn't there something else you should be working on right now?", 'Your father still loves and is in always with you. Remember that.', 'Before you can be reborn you must die.', 'It better to be the hammer than the nail.', 'You are admired by everyone for your talent and ability.', 'Save the whales. Collect the whole set.', 'You will soon discover a major truth about the one you love most.', 'Your life will prosper only if you acknowledge your faults and work to reduce them.', 'Pray to God, but row towards shore.', 'You will soon witness a miracle.', 'The early bird gets the worm, but the second mouse gets the cheese', "Help, I'm being held prisoner in a Chinese cookie factory.", 'Alas! The onion you are eating is someone else’s water lily.', "You are a persoon with a good sense of justice, now it's time to act like it.", 'You create enthusiasm around you.', 'There are big changes ahead for you. They will be good ones!', 'You will have many happy days soon.', 'Out of confusion comes new patterns.', "If you love someone enough and they break your heart, you can't stop yourself from still loving them again even after all that pain.", 'Look right...Now look left...Now look forward (do this really fast) do you feel any different? good you should feel dizzy.', 'Live like you are on the bottom, even if you are on the top.', "You will soon emerge victorious from the maze you've been traveling in.", "Do not judge a book by it's color.", 'Everything will come your way.', 'There is a time to be practical now.', 'Bend the rod while it is still hot.', "Darkness is only succesful when there is no light. Don't forget about light!", 'Acting is not lying. It is findind someone hiding inside you and letting that person run free.', 'You will be forced to face fear, but if you do not run, fear will be afraid of you.', "You are thinking about doing something. Don't do it, it won't help anything.", 'Your worst enemy has a crush on you!', 'Love Conquers all.', 'The phrase is follow your dreams. Not dream period.', 'stop nagging to your partner and take it day by day.', 'Do not think that me or my brothers have supreme control over what will happen to you.', 'Bad luck and misfortune will follow you all your days.', 'Remember the fate of the early Worm.', 'Begin your life anew with strength, grace and wonder.', 'Be a good friend and a fair enemy.', 'What goes around comes around.', 'Bad luck and misfortune will infest your pathetic soul for all eternity.', 'The best prophet of the future is the past', 'Movies have pause buttons, friends do not', 'Use the force.', 'Trust your intuition.', 'Encourage your peers.', 'Let your imagination wander.', 'Your pain is the breaking of the shell that encloses your understanding.', 'Patience is key, a wait short or long will have its reward.', "Tell them before it's too late...", 'A bird in the hand is worth three in the bush!!', 'Be assertive when decisive action is needed.', 'To determine whether someone is beautiful is not by looking at his/her appearance, but his/her heart.', 'Hope brings about a better future', "While you have this day, fill it with life. While you're in this moment, give it your own special meaning and purpose and joy.", 'Even though it will often be difficult and complicated, you know you have what it takes to get it done.', 'You can choose, right now and in every moment, to put your powerful and effective abilities to purposeful use. There is always something you can do, no matter what the situation may be, that will move your life forward.', 'IT IS NOT GOOD TO BE A USER BLESSINGS COME FROM BEING A GIVER NOT A TAKER.', 'Cookie says, "You crack me up"', 'You will prosper in the field of wacky inventions.', 'Your tongue is your ambassador.', 'The cure for grief is movement.', 'Love Is At Your Hands Be Glad And Hold On To It.', 'You are often asked if it is in yet.', 'Life to you is a bold and dashing responsibility.', 'Patience is a key to joy.', "A bargain is something you don't need at a price you can't resist.", 'Today is going to be a disasterous day, be prepared!', 'Stay to your inner-self, you will benefit in many ways.', 'Rarely do great beauty and great virtue dwell together as they do in you.', 'You are talented in many ways.', 'You are the master of every situation.', 'Your problem just got bigger. Think, what have you done.', 'If your cookie still in one piece, buy lotto.', 'Go with the flow will make your transition ever so much easier.', 'Tomorrow Morning,Take a Left Turn As Soon As You Leave Home', 'A metaphor could save your life.', "Don't wait for your ship to come in, swim out to it", 'There are lessons to be learned by listening to others.', 'If you want the rainbow, you have to tolerate the rain.', 'Volition, Strength, Languages, Freedom and Power rests in you.', 'TOO MANY PEOPLE VOLUNTEER TO CARRY THE STOOL WHEN ITS TIME TO MOVE THE PIANO', 'It takes more than a good memory to have good memories.', 'You are what you are; understand yourself before you react', "Word to the wise: Don't play leapfrog with a unicorn.........", 'Forgive your enemies, but never forget them.', 'Everything will now come your way', "Don't worry about the stock market. Invest in family.", 'Your fortune is as sweet as a cookie.', 'It is much easier to look for the bad, than it is to find the good', "If a person who has caused you pain and suffering has brought you, reconsider that person's value in your life", 'You are worth loving, you are also worth the effort it takes to love you', 'Never trouble trouble till trouble troubles you.', 'Get off to a new start - come out of your shell.', 'Life is a dancefloor,you are the DJ!', 'Cooperate with those who have both know how and integrith.', 'Minor aches today are likely to pay off handsomely tomorrow.', 'You are about to become $8.95 poorer. ($6.95 if you had the buffet)', 'Your mouth may be moving, but nobody is listening.', 'Focus in on the color yellow tomorrow for good luck!', 'The problem with resisting temptation is that it may never come again.', 'All your sorrows will vanish.', 'About time I got out of that cookie.', 'Love will lead the way.', 'The ads revenge is massive success', 'It is best to act with confidence, no matter how little right you have to it.', 'Soon, a visitor shall delight you.']

    @commands.command(name='zoltar', aliases=['z'])
    async def eightball(self, context):
        '''Zoltar geeft je een antwoord'''
        await context.send('👳_"{}"_👳'.format(choice(self.antwoorden)))
