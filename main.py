from discord.ext import commands

bot = commands.Bot("!")

@bot.event
async def on_message(message):
    lost = "perdi"

    if message.author == bot.user:
        return

    if "perdi" in message.content:
        await message.channel.send(lost)

    if "Perdi" in message.content:
        await message.channel.send(lost)

    if "jogo" in message.content:
        await message.channel.send(lost)

    if "Jogo" in message.content:
        await message.channel.send(lost)

    if "perdeu" in message.content:
        await message.channel.send(lost)

    if "Perdeu" in message.content:
        await message.channel.send(lost)

    if "perdemo" in message.content:
        await message.channel.send(lost)

    if "Perdemo" in message.content:
        await message.channel.send(lost)
        

bot.run()
