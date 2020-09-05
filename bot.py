import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

nero_caster_quotes = [
    '“When you say summer, it has to be a resort.\nWhen you say resort, it has to be a high-class hotel.\nWhen you say high-class hotel, it has to be a special-installation arena!\nNow, the golden theater was changed to everlasting summer specifications, and the Emperor Nero goes Prism In on the summer se---a! As such!\nTaking the sunlight on board the flowing water current!\nThis time for sure, my opera will resound on Chaldea!”\nActually, rumor goes that her affinity here is better than in the Saber Class.',
    'Height/Weight: 150cm・42kg\nSource: Historical Fact\nRegion: Rome\nAlignment: Chaotic・Summer\nGender: Female\nSurprisingly enough, even in the Caster Class her parameters do not change at all from when she is in the Saber Class (Noble Phantasm aside).',
    'A self-alleged almighty genius.\nWhile she would act as a cross-dressing beauty (or so she thinks) in the Saber Class, this time she is openly enjoying the summer sea without hiding the fact that she is a beautiful woman.\nThe 5th Roman Emperor who possessed a majestic sense of values that combined narcissism and philanthropy in the form of “I love myself, but also love the people around me”.\nMaking the utmost best out of the magecraft she learned from Simon Magus, the Emperor Nero perfected a Mystic Code - or rather, a Theatrical Code for her own use.\nThe pipe-organs that float beside her body convert her beautiful voice into attack power and lavishly random-fire lasers, fireworks, fire-bullets, etc.\nBy the way, why would a singing voice cause damage?\nNero herself does not notice that cruel truth.',
    'Golden Threatre Praised in Song\nRank: A\nType: Anti-Army\nMaximum Targets: 500 people\nLauda Lentum Domus Illustrius.\nJust when you think that wind instruments were added to the golden theater, it turns out that those pipes were all gunports.\nWhat sort of power of imagination produced this? Was the designer sane at all? Still, pipe-organs are sort of gunport-like. An opera stronghold born from such complicated circumstances.\nHaving obtained the Saint Graph of “one who sings”, Nero display her talents to maximum effect.\nIt ended up becoming a great outdoors stage that carries that singing voice not only inside the golden theater, but also towards its exterior.',
    'Emperor-Type Servant\nNero wearing a revealing swimsuit. Her singing at the marine theater is something to see, but everyone in the audience would have preferred to drown rather than listen. Less painful that way.'
]


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Umu!. Hi {member.name}, welcome to my Discord Server'
    )


@bot.command(name='random_quote', help='Responds with a random quote from Nero Caster')
async def nero_caster_random_quotes(ctx):
    response = random.choice(nero_caster_quotes)
    await ctx.send(response)


@bot.command(name='quote', help='Responds with a quote from Nero Caster')
async def nero_caster_quote(ctx, quote_number: int):
    response = nero_caster_quotes[quote_number]
    await ctx.send(response)


@bot.command(name='dm', help='I cant say something to you')
async def dm(ctx):
    message = 'umu'
    await ctx.author.send(message)


@bot.command(name='dm_user', help='I cant say something to someone else')
async def dm_user(ctx, user: discord.User, *, message=None):
    message = message or 'umu'
    await user.send(message)

bot.run(TOKEN)
