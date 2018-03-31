import discord
import unicodedata
from discord.ext import commands
import time
from motor.motor_asyncio import AsyncIOMotorClient
import motor.motor_asyncio
import datetime
import sys
import psutil
import asyncpg
from pymongo import MongoClient
import requests
import ftfy
import traceback
from discord.ext.commands import errors
import openweathermapy.core as weather
import platform
import copy
import asyncio
import os
import urllib.parse
from urllib.request import urlopen
import aiohttp
import json
import random
import io
import textwrap
import subprocess
import inspect
from urllib.parse import urlencode
from contextlib import redirect_stdout
from utils.config import *
from pyfiglet import figlet_format as ascii_format


class Music:
    def __init__(self, bot):
       self.bot = bot


    @commands.command()
    async def connect(self, ctx):
        '''Connects the bot to your current voice channel.'''
        if ctx.author.voice is None:
            return await ctx.send("Looks like you aren't connected to a voice channel yet! Where do I join?")
        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()
            await ctx.send(f"Successfully connected to Voice Channel **{ctx.author.voice.channel.name}**. :white_check_mark:")
        else:
            await ctx.voice_client.move_to(ctx.author.voice.channel)
            await ctx.send(f"Successfully connected to Voice Channel: **{ctx.author.voice.channel.name}**. :white_check_mark:")


    @commands.command()
    async def disconnect(self, ctx):
        '''Disconnects the bot to your current voice channel. Cya!'''
        if ctx.voice_client is None:
            await ctx.send("Looks like I'm not connected to a voice channel yet! Can't disconnect...:thinking:")
        else:
            await ctx.voice_client.disconnect()
            await ctx.send(f"Successfully disconnected from the voice channel. :white_check_mark:")


def setup(bot):
    bot.add_cog(Music(bot))