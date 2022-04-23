import discord
from tokenize import Token
Token = 'OTU5MzYxOTY5NTI4NDA2MDU2.YkaxdQ.hCYeTS5P_F3IiqJzGW_X1UTHcFs'

default_intents = discord.Intents.default()
default_intents.members = True

client = discord.Client(intents=default_intents)
@client.event

async def on_ready():
    print("Le bot est prêt !")
    
@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong")

@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(959366600975323158)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name}!")
 
@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()
    
client.run(Token)
