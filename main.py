import discord
import token
import asyncio

token = token.token()

client = discord.Client()

@client.event
async def on_ready():
  print("Bot Online!")

@client.event
async def on_member_join(member):
  channel = client.get_channel("***")
  msg = "Welcome {}".format(member.mention)
  await client.send_message(channel, msg)

@client.event
async def on_member_remove(member):
  channel = client.get_channel("***")
  msg = "Goodbye {}".format(member.mention)
  await client.send_message(channel, msg)

client.run(token)
