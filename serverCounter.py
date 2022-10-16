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

#client.run('ODcxODA4NDI2MjQwNTIwMjUz.YQgs3g.no-hyi7r-F-FH4QYp3RPbxlBwT0') #MrBot's Token
client.run('Nzc1NzEzMTA3NDQ3MjUwOTk1.X6qVIA.T-HS9T2CLHAPJPYjKtP_xpN0zdM') #Tony's Token
#client.run('OTMyNjU0OTE0MzQwMDI4NDY2.YeWIkw.giASQUx6XlyRtrocIUF2NStgVW0')
#client.run('OTQyMDgwNDY3MjQxNDEwNjMw.YgfSzg.oBwEgCwk5-3QiaVQ9qFVrbFnE0A')#elitex's Token


#client.run("OTM3MDA5NTExMzU5NzMzNzgw.YfVgHA.7RfhrkqAXNKI4mQFfE9beWN2Xkw")#Minecraft's Token