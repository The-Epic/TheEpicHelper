import discord
from discord.ext import commands
import json
import os
import random
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"TOKEN": "", "Prefix": "e!"}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)
token = configData["TOKEN"]
prefix = configData["Prefix"]
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix =prefix, intents = intents)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Helping The Epic Corner"))
    print('The Epic Helper is online')
#commands are below
@client.event
async def on_member_join(member):
    channel = client.get_channel(867202551324868618)
    await channel.send(f"Welcome {member} to {member.guild}!")
@client.command()
async def hello(ctx):
    await ctx.send('Hallo')
@client.command()
async def ping(ctx):
    await ctx.send(f'My ping is {round(client.latency * 1000)}ms')
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=25):
    await ctx.channel.purge(limit=amount + 1)
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    channel = client.get_channel(869216469198729216)
    await ctx.send(f'{member.mention} was banned.')
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    channel = client.get_channel(869216469198729216)
    await ctx.send(f'{member.mention} was kicked.')
@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            channel = client.get_channel(869216469198729216)
            await ctx.send(f'{member.mention} was unbanned.')
            return
@client.command()
async def announce(ctx, *, arg):
    channel = client.get_channel(867291997182230528)
    await channel.send(arg)
#commands will be above
client.run(token)