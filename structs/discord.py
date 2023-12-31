import os, discord, time
from discord.ext import commands
from structs import handler

client = commands.Bot(command_prefix=">", intents=discord.Intents.all())
channel = None

async def on_register(identifier):
    global channel
    if channel != None:
        await channel.send(identifier+" just connected.")
    pass

async def on_unregister(identifier):
    global channel
    if channel != None:
        await channel.send(identifier+" closed connection with the websocket.")

@client.event
async def on_message(message):
    global channel
    if message.content[0] != "!": return
    args = message.content[1:].split(" ")
    if args[0] == "here":
        handler.channel = message.channel
        channel = message.channel
        await message.channel.send("This channel has been designated to display messages from the websocket.")
    if len(args) > 0:
        for v in handler.all_triggers:
            if v[0] == args[0]:
                print("passing "+"trigger/"+v[0]+"/"+" ".join(args[1:]))
                await v[2].send("trigger/"+v[0]+"/"+" ".join(args[1:]))
    pass

@client.event
async def on_ready():   
    print('Discord bot ready')
