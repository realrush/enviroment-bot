import discord
import os
import random

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)











@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$selam'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("Bye!")
    elif message.content.startswith('!who are you'):
        await message.channel.send("!I am a discord chat bot!")
    elif message.content.startswith('!can you do complicated things?'):
        await message.channel.send("Not yet, I am a basic text bot.")
    elif message.content.startswith('what is your name'):
        await message.channel.send("You can call me bot.")
    elif message.content.startswith("!sendrandompicture"):
        # Send an image chatgpt is goated
        with open('github profile picture temp.jpg', 'rb') as f:
            await message.channel.send(file=discord.File(f, 'github profile picture temp.jpg'))

    elif message.content.startswith("!sendrandommem"):
        liste = os.listdir("resimler")
        secilenresim = random.choice(liste)
        with open (f"resimler/{secilenresim}", "rb") as f:
            resim = discord.File(f)
        await message.channel.send(file=resim)

    elif message.content.startswith('!helpenviroment'):
        await message.channel.send("Here is a video so you can see how to help the enviroment! https://www.youtube.com/watch?v=gUhxcdzRgLQ")
    elif message.content.startswith('!paperbin'):
        await message.channel.send("Paper goes to the blue bin")
    elif message.content.startswith('!metalbin'):
        await message.channel.send("Metal goes to the gray bin")
    elif message.content.startswith('!plasticbin'):
        await message.channel.send("Plastic goes to the yellow bin")
    elif message.content.startswith('!glassbin'):
        await message.channel.send("Glass goes to the green bin")
    elif message.content.startswith('!organicbin'):
        await message.channel.send("Other organic stuff goes to the orange bin")
    elif message.content.startswith('!unsaveingtrash'):
        await message.channel.send("The other trash goes to the black bin")









       
    else:
        await message.channel.send(message.content)






client.run("your client thing")
