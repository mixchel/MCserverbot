import os
import discord
import time 
from dotenv import load_dotenv
from discord.ext import commands
from mcstatus import JavaServer
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='>')
def get_ip():
    return (os.popen('grep server-ip ~/MCserver/server.properties').read())[10:]
server = JavaServer.lookup(get_ip())
@bot.command(name='ip')
async def ipcheck(ctx):
    await ctx.send(get_ip())
@bot.command(name='start')
async def start(ctx):
    os.system('~/MCserverbot/start.sh')
    await ctx.send('Starting Server...')
    for i in range (4):
        time.sleep(30)
        try:
            server.ping()
        except:
            started = 0
        else:
            await ctx.send('Server started sucesfully')
            started = 1
            break
    print(started)
    if started == 0:print("There was an error starting server")
@bot.command(name='stop')
async def stop(ctx):
    os.system('~/MCserverbot/stop.sh')
    await ctx.send('Server Stopped')
bot.run(TOKEN)


