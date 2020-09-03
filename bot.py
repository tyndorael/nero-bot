import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(f'{client.user} has connected to Discord!')
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Umu!. Hi {member.name}, welcome to my Discord Server'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    nero_caster_quotes = [
        '“When you say summer, it has to be a resort.\nWhen you say resort, it has to be a high-class hotel.\nWhen you say high-class hotel, it has to be a special-installation arena!\nNow, the golden theater was changed to everlasting summer specifications, and the Emperor Nero goes Prism In on the summer se---a! As such!\nTaking the sunlight on board the flowing water current!\nThis time for sure, my opera will resound on Chaldea!”\nActually, rumor goes that her affinity here is better than in the Saber Class.',
        'Height/Weight: 150cm・42kg\nSource: Historical Fact\nRegion: Rome\nAlignment: Chaotic・Summer\nGender: Female\nSurprisingly enough, even in the Caster Class her parameters do not change at all from when she is in the Saber Class (Noble Phantasm aside).',
        'A self-alleged almighty genius.\nWhile she would act as a cross-dressing beauty (or so she thinks) in the Saber Class, this time she is openly enjoying the summer sea without hiding the fact that she is a beautiful woman.\nThe 5th Roman Emperor who possessed a majestic sense of values that combined narcissism and philanthropy in the form of “I love myself, but also love the people around me”.\nMaking the utmost best out of the magecraft she learned from Simon Magus, the Emperor Nero perfected a Mystic Code - or rather, a Theatrical Code for her own use.\nThe pipe-organs that float beside her body convert her beautiful voice into attack power and lavishly random-fire lasers, fireworks, fire-bullets, etc.\nBy the way, why would a singing voice cause damage?\nNero herself does not notice that cruel truth.',
        'Golden Threatre Praised in Song\nRank: A\nType: Anti-Army\nMaximum Targets: 500 people\nLauda Lentum Domus Illustrius.\nJust when you think that wind instruments were added to the golden theater, it turns out that those pipes were all gunports.\nWhat sort of power of imagination produced this? Was the designer sane at all? Still, pipe-organs are sort of gunport-like. An opera stronghold born from such complicated circumstances.\nHaving obtained the Saint Graph of “one who sings”, Nero display her talents to maximum effect.\nIt ended up becoming a great outdoors stage that carries that singing voice not only inside the golden theater, but also towards its exterior.',
        'Emperor-Type Servant\nNero wearing a revealing swimsuit. Her singing at the marine theater is something to see, but everyone in the audience would have preferred to drown rather than listen. Less painful that way.'
    ]

    if message.content == '!quote':
        response = random.choice(nero_caster_quotes)
        await message.channel.send(response)
    elif message.content == '!neptune':
        await message.channel.send('https://www.youtube.com/watch?v=eoBn7X_Zpws')
    elif message.content == '!raise-exception':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)
