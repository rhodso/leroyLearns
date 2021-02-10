import discord
import datetime
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import platform
import datetime
import random
import os

prefix = "?"

#Def log method
def log(Message):
    print(str(datetime.datetime.now())+ '   ' + str(Message))

#Def Method to read token from the file
def getToken():
    #If token file doesn't exist, create it
    if(not os.path.exists("token.txt")):
        tFile = open("token.txt", "w+")
        tFile.write("")
        tFile.close()
    
    #Read file
    tokenFile = open('token.txt','r')
    token = tokenFile.read()
    if(token == ""):
        log("Token empty, exiting...")
        quit(0)
    return token
    
#Define client
client = Bot(description='', command_prefix=prefix, pm_help = False)

#Startup sequence
@client.event
async def on_ready():
    log('Current Discord.py Version: ' + str(discord.__version__))
    log('Current Python Version: ' + str(platform.python_version()))
    log('Initialising...')
    log('Logged in as '+client.user.name+' (ID:'+str(client.user.id)+')')
    log('')
    log('Ready!')
    return await client.change_presence(status=discord.Status.idle, activity=discord.Game("with myself")) 

#Commands
@client.event
async def on_message(message):
    if(message == prefix + "ping"):
        await message.channel.send("Pong!")



#Run bot
log("Starting bot...")
client.run(str(getToken()))