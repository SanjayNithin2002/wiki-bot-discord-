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
    if message.author == client.user:
        return

    if message.content.startswith("wiki"):
        a = message.content[4:]
        result = wiki(a)
        await message.channel.send(result)
        

    if message.content.startswith("-wiki"):
        await message.channel.send("Hey!What do you guys wanna know")

keep_alive()
client.run(os.getenv("TOKEN"))