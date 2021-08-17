import time
import discord
from discord.ext import commands
from random import randrange

from discord.utils import get
from discord import Role
from random import shuffle

from discord.ext.commands import Bot
from constants import token


bot = discord.Client()
welcome_msg_id = 876102121219588187

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == welcome_msg_id:
        reactor = payload.user_id
        if payload.emoji.name == '✅':
            role_id = 876139733565198377
            role = get(payload.member.guild.roles, id=role_id)
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🔞':
            role_id = 876104434348851252
            role = get(payload.member.guild.roles, id=role_id)
            await payload.member.add_roles(role)


        

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.message_id == welcome_msg_id:
        reactor = payload.user_id
        if payload.emoji.name == '✅':
            role_id = 876104434348851252
            role = get(payload.member.guild.roles, id=role_id)
            await payload.member.remove_roles(role)
bot.run(token)
