import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant


chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

load_dotenv()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('luca' or 'Luca'):
        response = chatbot.request(message.content[6:])
        await message.channel.send(response)

    if message.content == 'dme':
        await message.author.send("Hola bro")

    if message.content == "info":
        embed = discord.Embed(
            title="LucasD'sNotes",
            description="Información de comandos",
            color=0xbd42ff
        )
        embed.set_author(
            name="MOONee", icon_url="https://pbs.twimg.com/media/FPRqPjraMAAnprt?format=jpg&name=large")
        embed.set_author(
            name="Shiro", icon_url="https://blogger.googleusercontent.com/img/a/AVvXsEguuH30G59vBcUcffKmon1OsOT3_gtxiIo3DndUVzvE62yo6sg1oRa418fXw2N9yGTgwTXtd3Xquw4kl_8qpBlCDEN6V2a_oG-f6mafuSKigqNUWiotgZNauAuSC6vroirAj4eMSmnJ-k73ArpnP-GwCVecWVCfukizUoY6k7Lu0E3UQSmZIebhYVtOqw=w640-h426")
        embed.set_thumbnail(url="https://pbs.twimg.com/media/FQDjuVSagAMJUry?format=jpg&name=4096x4096")
        embed.add_field(name="info", value="muestra los comandos", inline=True)
        embed.add_field(name="hola", value="Saluda al usuario", inline=True)
        embed.set_footer(text="Este bot fue creado el 20 de mayo de 2022")
        # await ctx.send(embed=embed)

        await message.channel.send(content=None, embed=embed)


@client.event
async def on_ready():
  activity = discord.Game(name="Netflix", type=3)
  await client.change_presence(status=discord.Status.idle, activity=activity)
  print('Look at this Notes, {0.user}'.format(client))
  channel = client.get_channel(975942882454286356)
  c= 'Escribe info para ver los comandos disponibles'
  await channel.send(c.capitalize())

@client.event
async def on_connect():
    print("Bot connected to the server!")

    #channel = client.get_channel(id)
    #await channel.send("Acá ando")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Welcome to hell {member}!")



client.run(os.getenv('TOKEN'))
