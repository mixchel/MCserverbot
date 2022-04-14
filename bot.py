import os
import discord
import time 
from dotenv import load_dotenv
from discord.ext import commands
from mcstatus import MinecraftServer
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='>')
def get_ip():
    return (os.popen('ssh michel@192.168.15.88 grep server-ip ~/MCserver/server.properties').read())[10:]
server = MinecraftServer.lookup(get_ip())
@bot.command(name='ip')
async def ipcheck(ctx):
    await ctx.send(get_ip())
@bot.command(name='start')
async def start(ctx):
    os.system('ssh michel@192.168.15.88 ~/MCserverbot/start.sh')
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
    os.system('ssh michel@192.168.15.88 ~/MCserverbot/stop.sh')
    await ctx.send('Server Stopped')
bot.run(TOKEN)


