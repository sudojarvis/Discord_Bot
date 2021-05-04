import json
import os

import discord
import requests
from googlesearch import search

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "-" + json_data[0]['a']
    return (quote)


def today_quote():
    response = requests.get("https://zenquotes.io/api/today")
    json_data = json.loads(response.text)
    quotes = json_data[0]['q'] + "-" + json_data[0]['a']
    return (quotes)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if message.content.startswith('rquotes'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('tquotes'):
        quotes = today_quote()
        await message.channel.send(quotes)

    if message.content.startswith('hello') or message.content.startswith('Hello'):
        await message.channel.send('Hii! I am Bot')

    if message.content.startswith('Hi') or message.content.startswith('hi'):
        await message.channel.send('Hello! I am Bot')

    if message.content.startswith('@ '):
        text = str(message.content).split(' ')
        searchContent = ' '.join([elem for elem in text])
        for j in search(searchContent, tld="co.in", num=1, start=5, pause=2, stop=5):
            await message.channel.send(j)
client.run(os.getenv('TOKEN'))