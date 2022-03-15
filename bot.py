import os
import discord 
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
@client.event
async def on_message(message):
    if message.content == '/start':
        os.system('~/MCserver/start.sh')
        await message.channel.send('Server Started')
    if message.content == '/stop':
        os.system('~/MCserver/stop.sh')
        await message.channel.send('Server Stopped')
client.run(TOKEN)
