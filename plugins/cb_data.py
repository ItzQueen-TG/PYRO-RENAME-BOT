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
ADMINS = int(5195423974)
logg_channel = int(os.environ.get("LOG_CHNNEL", "-1001479558698"))

@Client.on_message(filters.private & filters.command(['rrestart']) & filters.user(int("5195423974")))
async def restart(client, message):
    msg = await message.reply_text("Trying to restarting....."
    )  
    await asyncio.sleep(1)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)


BOT_STATUS = "0"
status = set(int(x) for x in (BOT_STATUS).split())

@Client.on_message(filters.private & filters.command("add"))
async def approve_join_requests(client: User, message):
    public_chat = await client.ask(message.from_user.id, "**❪ CHOOSE PUBLIC GROUP ❫**\n\nEnter the username of the public GROUP (e.g. @publicGROUP)")
    public_chat_id = (await client.get_chat(public_chat.text)).id
    target_chat = await client.ask(message.from_user.id, "**❪ CHOOSE TARGET GROUP ❫**\n\nEnter the username of the target channel (e.g. @myGROUP)")
    target_chat_id = (await client.get_chat(target_chat.text)).id
 
    join = 0
    error = 0
    members = client.get_chat_members(public_chat_id)
    m = await client.send_message(chat_id=message.from_user.id, text="`processing...`")
    for member in members:
        try:
            client.add_chat_members(target_chat_id, member.user.id)
            join += 1
            print(f"Approved join request for user {member.user.id}")
            await m.edit(f"{join}\n\n{error}")
        except Exception as e:
            print(f"User {member.user.id} is already a member of the channel")
            error += 1
            await m.edit(f"{join}\n\n{error}")
            continue
    message.reply_text("completed {join}/ {error}")

@Client.on_message(filters.private & filters.command(['frestart']) & filters.user(int("5195423974")))
async def restart(client, message):
    msg = await message.reply_text("Trying to restarting....."
    )  
    await asyncio.sleep(1)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.private & filters.command("set"))                        
async def set_tumb(bot, msg):
    replied = msg.reply_to_message
    if not replied:
        await msg.reply("use this command with Reply to a photo")
        return
    if not msg.reply_to_message.photo:
       await msg.reply("Oops !! this is Not a photo")
       return
    Tumb = msg.reply_to_message.photo.file_id
    temp.THUMBNAIL = Tumb
    return await msg.reply(f"Temporary Thumbnail saved✅️ \nDo You want permanent thumbnail. \n\n`{Tumb}` \n\n👆👆 please add this id to your server enviro with key=`THUMBNAIL`")            


@Client.on_message(filters.private & filters.command("view"))                         
async def del_tumb(bot, msg):
    if temp.THUMBNAIL:
        await msg.reply_photo(photo=temp.THUMBNAIL, caption="this is your current thumbnail")
    else:
        await msg.reply_text(text="you don't have any thumbnail")

@Client.on_message(filters.chat(F_CHANNEL) & (filters.document | filters.video))
async def doc(bot, msg):
     media = msg.document or msg.audio or msg.video
     og_media = getattr(msg, msg.media.value)
     filename = og_media.file_name
     value = 2090000000
     if value > media.file_size:
         svm = re.sub(r"\[SVM\]\.", "", filename)
         gc = re.sub(r"\[GC\]\.", "", svm)
         a_name = re.sub(r'@CC_Links\.', '', gc)
         name = re.sub(r'\[CC\]\.*', '', a_name)
         result = re.sub(r'@CC_', '', name)
         a_result = re.sub(r'@HEVCHubX\.', '', result)
         b_result = re.sub(r'\[@Anime Clan\]\s*', '', a_result)
         w_result = re.sub(r'@WMR_\s*', '', b_result)
         c_result = re.sub(r'@\w+\s*', '', w_result)
         s_result = re.sub(r'\s', '.', c_result)
         m_result = re.sub(r'\[MM\]\.*', '', s_result)
         p_result = re.sub(r'\[PFM\]\.', '', m_result)
         d_result = re.sub(r"\]", "", p_result)
         e_result = re.sub(r"\[", "", d_result)
         f_a= re.sub(r"\(|\)", "", e_result)
         new_name = f_a
         file = msg.document or msg.video
         file_path = f"downloads/{new_name}"
         currentTime = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
         last_update = currentTime.strftime(f"%I:%M:%S %p")
         sts = await bot.send_message(chat_id=ADMINS, text=f"Trying to Download 📩\n\n`{new_name}`\n\nLᴀsᴛ ᴜᴘᴅᴀᴛᴇᴅ ɪɴ:- `{last_update}`")
         c_time = time.time()
         try:
     	    path = await bot.download_media(message = file, progress=progress_message, progress_args=(f"Downloading 📩 `{new_name}`", sts, c_time))
         except Exception as e:
     	     await ms.edit(e)

         splitpath = path.split(f"/downloads/")
         dow_file_name = splitpath[1]
         old_file_name =f"downloads/{dow_file_name}"
         os.rename(old_file_name,file_path)
         if CAPTION:
             try:
                 caption = c_caption.format(filename=new_filename, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))
             except Exception as e:
                 await sts.edit(text=f"Your caption Error unexpected keyword ●> ({e})")
                 return 
         else:
             cap = f"`{new_name}`"
         raw_thumbnail = temp.THUMBNAIL 
         if raw_thumbnail:
            og_thumbnail = await bot.download_media(raw_thumbnail)
         else:
             og_thumbnail = await bot.download_media(og_media.thumbs[0].file_id)
         currentTime = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
         last_update = currentTime.strftime(f"%I:%M:%S %p")
         await sts.edit(f"Trying to Uploading 📤\n\n`{new_name}`\n\nLᴀsᴛ ᴜᴘᴅᴀᴛᴇᴅ ɪɴ:- `{last_update}`")
         c_time = time.time()
         try:
             await bot.send_document(
                       T_CHANNEL, 
                       document=file_path,
                       thumb=og_thumbnail, 
                       caption=cap,
                       progress=progress_message, 
                       progress_args=(f"Uploading 📤\n\n`{new_name}`", sts, c_time))
         except Exception as e:  
             print(e)
             await sts.delete()
             return               
         try:
             os.remove(file_path)
             os.remove(og_thumbnail)
         except:
             pass
         await sts.delete()
         await msg.delete()


async def progress_message(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 15.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)     
        currentTime = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
        last_update = currentTime.strftime(f"%I:%M:%S %p")                
        progress = "\n{0}{1}".format(
            ''.join(["▣" for i in range(math.floor(percentage / 5))]),
            ''.join(["▢" for i in range(20 - math.floor(percentage / 5))]))                                  
        tmp = progress + PROGRESS_BAR.format(
            a=round(percentage, 2),
            b=humanbytes(current),
            c=humanbytes(total),
            d=humanbytes(speed),
            f=estimated_total_time if estimated_total_time != '' else "0 s",
            g=last_update)                        
        try:
            await message.edit(text="{}\n{}".format(ud_type, tmp))         
        except:
            pass

def humanbytes(size):
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
          ((str(hours) + "h, ") if hours else "") + \
          ((str(minutes) + "m, ") if minutes else "") + \
          ((str(seconds) + "s, ") if seconds else "") + \
          ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
