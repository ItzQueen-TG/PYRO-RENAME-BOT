import re
import os 
import math
import time
import sys
import humanize
import asyncio
import datetime
import pytz

from pyrogram import Client, filters, enums
from pyrogram.types import *
from pyrogram.errors import FloodWait
from config import temp
from main import User

currentTime = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
last_update = currentTime.strftime(f"%I:%M:%S %p")


CAPTION = os.environ.get('CAPTION')
T_CHANNEL = int(os.environ.get("T_CHANNEL", "-1001837941527"))
F_CHANNEL = int(os.environ.get("F_CHANNEL", "-1001737494519"))
R_LOG = int(os.environ.get("FF_CHANNEL", "-1001862098106"))
PROGRESS_BAR = "\n\n📁 : {b} | {c}\n🚀 : {a}%\n⚡ : {d}/s\n⏱️ : {f}\n\nLᴀsᴛ ᴜᴘᴅᴀᴛᴇᴅ ɪɴ:- {g}"

U_CHANNEL = int(os.environ.get("U_CHANNEL", "-1001815935001"))

logg_channel = int(os.environ.get("LOG_CHNNEL", "-1001479558698"))

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(int("5195423974")))
async def restart(client, message):
    msg = await message.reply_text("Trying to restarting....."
    )  
    await asyncio.sleep(1)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)


BOT_STATUS = "0"
status = set(int(x) for x in (BOT_STATUS).split())

@User.on_message(filters.chat(U_CHANNEL) & (filters.document | filters.video))
async def autost(bot, msg):
    media = msg.document or msg.audio or msg.video
    og_media = getattr(msg, msg.media.value)
    filename = og_media.file_name
    new_name = filename
    cap = f"`{new_name}`"
    try: 
        await User.copy_message(F_CHANNEL, U_CHANNEL, msg.id)
        await asyncio.sleep(1)
        try:
            status.add(40)
        except:
            pass
        if 40 in status:
            await asyncio.sleep(status)
            await User.copy_message(F_CHANNEL, U_CHANNEL, msg.id)
        else: 
            s_time = status + 40
            await asyncio.sleep(s_time)
            await User.copy_message(F_CHANNEL, U_CHANNEL, msg.id)
        await asyncio.sleep(1)
        try:
            status.remove(40)
        except:
            pass
        try:
            status.add(40)
        except:
            pass
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await User.copy_message(F_CHANNEL, U_CHANNEL, msg.id)
        await asyncio.sleep(1)
        try:
            status.add(40)
        except:
            pass
        if 40 in status:
            await asyncio.sleep(status)
            await User.copy_message(F_CHANNEL, U_CHANNEL, msg.id)
        else: 
            s_time = status + 40
            await asyncio.sleep(s_time)
            await User.copy_message(F_CHANNEL, U_CHANNEL, msg.id)
        await asyncio.sleep(1)
        try:
            status.remove(40)
        except:
            pass
        try:
            status.remove(40)
        except:
            pass
