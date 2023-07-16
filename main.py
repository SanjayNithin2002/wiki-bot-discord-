import discord
import os
import wikipediaapi
import asyncio
from keep_alive import keep_alive

intents = discord.Intents.default() 
intents.message_content = True
client = discord.Client(intents=intents)
def wiki(a):
  wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='Your_User_Agent')
  page_py = wiki_wiki.page(a)
  result = page_py.summary
  if result == "": 
     page_py = wiki_wiki.page(a.title())
     result = page_py.summary
  return (result)


@client.event
async def on_ready():
  print("We logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("wiki"):
        a = message.content[4:]
        result = await asyncio.to_thread(wiki, a) # Use `await` to properly await the function
        a = a.title()
        embed = discord.Embed(title=a, description=result, color=0x00CED1)
        await message.channel.send(embed=embed)

      
        

    

keep_alive()

bot_token = os.getenv('TOKEN')
if bot_token:
    client.run(bot_token)
else:
   print("The bot token is invalid.")