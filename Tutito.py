import discord

TOKEN = 'NDU1MjUxMTk2OTgzMjQ2ODY4.Df5Sbg.bVLGWCj5dPVQsKYa-RFoUVw5yKA'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello :P {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
