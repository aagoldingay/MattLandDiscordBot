import discord
import asyncio

client = discord.Client()
voice = None

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	print("Hello, world")

client.run('Mzc5MTIwNzcyNTY1ODI3NTg0.DOlgFQ.9-qB7SXIJ7Lvqbpkn9GYDm6uU6A')