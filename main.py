import discord
from datetime import datetime, timedelta
from discord.ext import commands
import streamlit as st

intents = discord.Intents(members=True)
bot = commands.Bot(command_prefix='#', intents=intents)

token = st.secrets["TOKEN"] 

print("sugma")



bot.run(token)
