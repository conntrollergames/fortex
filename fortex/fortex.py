import discord
import asyncio
import random

#hier abkürzungen
client = discord.Client()
messageemot = None
minutes = 0
controller_games = "475343857261740033"
msgid = None
KnightRiders = "447743672369545226"
msguser = None
#hier abkürzungen


#print commands
@client.event
async def on_ready():
    print("Eingellogt als")
    print(client.user.name)
    print(client.user.id)
    print("------------")
    await client.change_presence(game=discord.Game(name="closed beta"))
#print commands

#naricht schreiben
@client.event
async def on_message(message):
    if message.content.lower().startswith("!help"):
     await client.send_message(message.channel, "\n"
                                                "**__Fortex - Hilfe menü__\n" 
                                                "!help - zeigt dir das an.\n"
                                                "!server - zeigt dir mein Server.\n"
                                                "\n"
                                                "Ich gebe dir Reaktionen, falls du was von dem schreibst. ✏️\n" 
                                                "\n"
                                                "Hallo = ✌️️️ \n"
                                                "Ruf mich an = thumbsup🤙**")

    if message.content.lower().startswith('hallo'):
        await client.add_reaction(message, '✌')
    if message.content.lower().startswith("ruf mich an"):
        await client.add_reaction(message, "🤙")
    if message.content.lower().startswith("!help"):
        await client.add_reaction(message, "👍")
    if message.content.lower().startswith("!game") and message.author.id == controller_games:
        game = message.content[6:]
        await client.send_message(message.channel, "mein status hat sich zu " + game + " geändert")
        await client.change_presence(game=discord.Game(name=game))
    if message.content.lower().startswith(".server"):
        await client.add_reaction(message, "👍")
    if message.content.lower().startswith(".server"):
         await client.send_message(message.author, "https://discord.gg/NwCNPQ")

    if message.content.startswith('!join'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Kein Voice channel gefunden.")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('!quit'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "Ich bin zur zeit nicht connected.")
        except Exception as Hugo:
         await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))


client.run("NDg0NzA1MDg3NTUwMjU5MjAw.DnvoOw.Ypt3oQjIClNIsAzUaQak_SoB4IU") #hier aktieviert der bot sich