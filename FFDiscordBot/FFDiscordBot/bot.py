#https://realpython.com/how-to-make-a-discord-bot-python/
#ideas: connect 4 bot
#assign roles to members using reactions
#picture among us

import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import random
from r_strs import r_strs


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    GUILD = os.getenv('DISCORD_GUILD')
    bot = commands.Bot(command_prefix='!')
    """
    @bot.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        for guild in client.guilds:
            if guild.id == GUILD:
                print('Located guild')
                break

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')"""

    

    @bot.command(name='hey')
    async def say_hi(ctx):
        await ctx.send("Hello! Good day to you.")

    @bot.command(name='rng', help = 'Gives random number (no arguments -> 6 sided dice)')
    async def roll(ctx, start : int = 1, end: int = 6):
        await ctx.send(r_strs.MAYTHEODDS + str(random.choice(range(start, end+1))))

    @bot.command(name='create-channel', help = 'Creates new text channel')
    async def create_channel(ctx, channel_name = r_strs.DEFAULT_CHANNEL_NAME):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            await guild.create_text_channel(channel_name, category = discord.utils.get(guild.categories, name = r_strs.BOT_TEXTCHANNEL))
        else:
            await ctx.send(r_strs.CHANNEL_EXISTS + channel_name)
            
    @bot.command(name='delete-channel', help = 'Deletes text channel')
    #@commands.has_role('Admin')
    async def delete_channel(ctx, channel_name = r_strs.DEFAULT_CHANNEL_NAME):
        guild=ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            await ctx.send(r_strs.CHANNEL_EXISTS + channel_name)
        elif channel_name in r_strs.ILLEGAL_CHANNELS:
            await ctx.send(r_strs.TRYNA_BE_SNEAKY)
        else:
            await existing_channel.delete()
            
    @bot.command(name='new-role', help = 'Creates a new role for groups people want to get pinged for')
    async def new_role(ctx, role_name):
        guild=ctx.guild
        existing_role = discord.utils.get(guild.roles, name= role_name)
        if role_name in r_strs.ILLEGAL_ROLES:
            await ctx.send(r_strs.TRYNA_BE_SNEAKY)
        elif not existing_role:
            role_assign_channel = discord.utils.get(guild.channels, name=r_strs.ASSIGN_ROLES)
            reaction = random.choice(range(len(r_strs.REACTIONS)))
            new_role = await guild.create_role(name = role_name)
            sent_message = await role_assign_channel.send(r_strs.NEWROLE_1 + r_strs.REACTIONS[reaction] + r_strs.NEWROLE_2 + role_name + '\n' + r_strs.NEWROLE_3 + new_role.mention)
            await sent_message.add_reaction(r_strs.REACTION_CODE[reaction])
        else:
            await ctx.send(r_strs.ROLE_ALREADY_EXISTS)


    @bot.event
    async def on_raw_reaction_add(payload):
        guild = bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        if channel.name == r_strs.ASSIGN_ROLES:
            message = await channel.fetch_message(payload.message_id)
            emote, role_name = r_strs.processRoleMessage(message.content)
            guild_user = await guild.fetch_member(payload.user_id)
            if payload.emoji.name == emote and payload.user_id != bot.user.id:
                await guild_user.add_roles(discord.utils.get(guild.roles, name=role_name))

    @bot.event
    async def on_raw_reaction_remove(payload):
        guild = bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        if channel.name == r_strs.ASSIGN_ROLES:
            message = await channel.fetch_message(payload.message_id)
            emote, role_name = r_strs.processRoleMessage(message.content)
            guild_user = await guild.fetch_member(payload.user_id)
            if payload.emoji.name == emote:
                role = discord.utils.get(guild.roles, name=role_name)
                await guild_user.remove_roles(role)
                if len(role.members) == 0:
                    await role.delete()
                    await message.delete()
            
            
            

        
    bot.run(TOKEN)
