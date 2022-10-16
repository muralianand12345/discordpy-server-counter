import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------')
    print(len(client.guilds))
    print('------')
    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)

client.run('') #Tony's Token
