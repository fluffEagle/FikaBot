# Fikabot.py
import os
import random
import discord
import asyncio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content.upper() == 'FIKA!':
        guild = message.guild
        fikaChannel = discord.utils.find(lambda x: x.name == "Fika", guild.channels)
        
        for voiceChannel in guild.voice_channels:
            if voiceChannel.name != "Fika":
                roleName = "Fika_" + voiceChannel.name
                if not discord.utils.get(guild.roles, name=roleName):
                    await guild.create_role(name=roleName)

                role = discord.utils.get(guild.roles, name=roleName)
                    
                memberIds = voiceChannel.voice_states.keys()
                for memberId in memberIds:
                    member = await guild.fetch_member(memberId)
                    await member.add_roles(role)
                    await member.move_to(fikaChannel)
        await message.channel.send("fika starts now!")
        #await asyncio.sleep(15) # 15 min fika time
    
    if message.content.upper() == 'END FIKA':
        guild = message.guild
        await message.channel.send("fika ends now!")
        fikaChannel = discord.utils.find(lambda x: x.name == "Fika", guild.channels) #does this refresh moved users??
        memberIds = fikaChannel.voice_states.keys()
        for memberId in memberIds:
            member = await guild.fetch_member(memberId)
            print(member.display_name)
            for voiceChannel in guild.voice_channels:
                if voiceChannel.name != "Fika":
                    roleName = "Fika_" + voiceChannel.name
                    if not discord.utils.get(guild.roles, name=roleName):
                        await guild.create_role(name=roleName)
                    role = discord.utils.get(guild.roles, name=roleName)
                    if role in member.roles:
                        await member.remove_roles(role)
                        await member.move_to(voiceChannel)


        
            #if voiceChannels.members != None:
            #    await member.move_to(fikaChannel)
            #else:
            #    print(f'member was none')
        #await message.author.move_to(fikaChannel)
        
        
        # sleep 15 min
        # move everyone back
        
        #response = random.choice(brooklyn_99_quotes)
        #await message.channel.send(response)

client.run(TOKEN)
