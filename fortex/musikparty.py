import discord
import asyncio

client = discord.client

@client.event
async def on_ready():
    print("musik bot on")
    print("============")


@client.event
async def on_message(message):
    if message.conntent.lower().startswith("!join"):
        channel = message.author.voice.voic_channel
        await client.send_message(message.channel, "tetdd")


client.run("NDg0NzA1MDg3NTUwMjU5MjAw.Dn2tNA.EWMYnnSfnmGcjB-PTZnhfq15NQY")

