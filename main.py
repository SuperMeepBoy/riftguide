import json

import discord
from discord.ext import commands


config = json.load(open('./config.json', 'r', encoding='utf-8'))
TOKEN = config['token']
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


# Command
@client.command()
async def helloworld(ctx, arg):
    champion = arg.split()[0]
    role = arg.split()[1]
    url = f"https://u.gg/lol/champions/{champion}/build?role={role}"
    await ctx.send(url)


client.run(TOKEN)
