import discord
import os
from wikipediaapi import Wikipedia
from keep_alive import keep_alive

client = discord.Client()
def wiki(a):
  wiki_wiki = Wikipedia('en')
  page_py = wiki_wiki.page(a)
  result = page_py.summary[0:400].split('.')
  result ='.'.join(result[:-1]) + '.'
  return (result)


@client.event
async def on_ready():
  print("We logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user: return
    if message.content.startswith("wiki"):
      a = message.content[4:]
      result = wiki(a)
      a = a.title()
      embed=discord.Embed(title=a, description=result, color=0x00CED1)
      await message.channel.send(embed=embed)
      
        

    

keep_alive()
client.run(os.getenv("TOKEN"))
