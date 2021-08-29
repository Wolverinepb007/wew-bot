import discord
import os
import requests
import json
from keep_alive import keep_alive
import asyncio

client = discord.Client()


def get_jokes():
    response = requests.get("https://official-joke-api.appspot.com/jokes/ten")
    json_data = json.loads(response.text)
    jokes = json_data[0]['setup'] + " Ans: " + json_data[0]['punchline']
    return (jokes)


def get_poem():
    response = requests.get("https://poetrydb.org/random/13")
    json_data = json.loads(response.text)
    poem = json_data[0]['lines']
    ath = "------" + json_data[0]['author']
    return (poem, ath)


def get_que():
    response = requests.get("./questions.json")
    json_data = json.loads(response.text)
    que = json_data[1]['question']
    return (que)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$wewjoke'):
            jokes = get_jokes()
            await message.channel.send(jokes)

        if message.content.startswith('$wewpoem'):
            poem = get_poem()
            ath = get_poem()
            await message.channel.send(poem)
            await message.channel.send(ath)

        if message.content.startswith('$wewt'):
            que = get_que()
            await message.channel.send(que)

        if message.content.startswith('$fact'):
            await message.channel.send("Wolverine is the best.")

        if message.content.startswith('$fact2'):
            await message.channel.send("Wolverine is awesome.😂")
        
        if message.content.startswith('hello'):
            await message.channel.send("Hello {0.author.mention}".format(message))


keep_alive()
client.run(os.getenv('TOKEN'))
