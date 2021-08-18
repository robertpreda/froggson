import time
import discord
from discord.ext import commands
from random import randrange

from discord.utils import get
from discord import Role
from random import shuffle

from discord.ext.commands import Bot
from constants import token


intents = discord.Intents.all()
bot = discord.Client(intents=intents)
welcome_msg_id = 876102121219588187


roles_id_map = {
    '✅': 876139733565198377,
    '🔞': 876104434348851252,
    '🧱': 877320383236288542,
    'valorant': 877548236410343465,
    'league': 877547947955470357
}

@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == welcome_msg_id:
        ########## FOR DEBUGGING PURPOSES ##########
        ########## UNCOMMENT IF NEEDED #############
        # print(payload.emoji.name)
        ############################################
        try:
            role_id = roles_id_map[payload.emoji.name]
            role = get(payload.member.guild.roles, id=role_id)
        except KeyError:
            role = None

        if role != None:
            await payload.member.add_roles(role)


        

@bot.event
async def on_raw_reaction_remove(payload):
    guild  = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.message_id == welcome_msg_id:
        try:
            role_id = roles_id_map[payload.emoji.name]
            role = get(guild.roles, id=role_id)
        except KeyError:
            role = None
        # if payload.emoji.name == '✅':
        #     role_id = 876104434348851252
        #     role = get(payload.member.guild.roles, id=role_id)
        await member.remove_roles(role)
bot.run(token)
