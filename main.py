import discord
import os
import wikipediaapi
import asyncio
import concurrent.futures

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
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="wiki"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("wiki"):
        a = message.content[4:]
        result = await run_in_thread(wiki, a)  # Use the alternative run_in_thread function

        if result: 
           await message.add_reaction("👍")
           a = a.title()
           embed = discord.Embed(title=a, description=result, color=0xC8E6C9)
           await message.channel.send(embed=embed)
           
        else:
           await message.add_reaction("👎")
           embed = discord.Embed(title="Page Unavailable", description="Try different prompt.", color=0xFFCDD2)
           await message.channel.send(embed=embed)

async def run_in_thread(func, *args, **kwargs):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(executor, func, *args, **kwargs)


bot_token = os.getenv("TOKEN")
if bot_token:
    client.run(bot_token)
else:
   print("The bot token is invalid.")