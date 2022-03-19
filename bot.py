import os
import discord 
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='>')

@bot.command(name='ip')
async def ipcheck(ctx):
    await ctx.send(os.popen('grep server-ip ~/MCserver/server.properties').read())
@bot.command(name='start')
async def start(ctx):
    os.system('~/MCserverbot/start.sh')
    await ctx.send('Server Started')
@bot.command(name='stop')
async def stop(ctx):
    os.system('~/MCserverbot/stop.sh')
    await ctx.send('Server Stopped')
bot.run(TOKEN)

