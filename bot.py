import os
import discord
import time 
from dotenv import load_dotenv
from discord.ext import commands
from mcstatus import JavaServer
# Setting up intents
my_intents = discord.Intents.default()
my_intents.message_content = True
load_dotenv()
#Loading Token
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=my_intents)
bot = commands.Bot(command_prefix='>', intents=my_intents)
def get_ip():
    return "104.248.230.246"
def server_is_on():
    try:
        server.ping()
    except TimeoutError:
        return 0
    else:
        return 1
# Defining the Server
server = JavaServer.lookup(get_ip())
@bot.command(name='ip')
async def ipcheck(ctx):
    await ctx.send(get_ip())
@bot.command(name='start')
async def start(ctx):
    if not server_is_on():
        os.system('~/MCserverbot/start.sh')
        await ctx.send('Starting Server...')
        started == 0
        for i in range (4):
            time.sleep(30)
            if server_is_on():
                await ctx.send('Server started sucesfully')
                started = 1
                break
        if started == 0:print("There was an error starting server")
    else:
        await ctx.send("Server was already on")
@bot.command(name='stop')
async def stop(ctx):
    os.system('~/MCserverbot/stop.sh')
    await ctx.send('Server Stopped')
bot.run(TOKEN)


