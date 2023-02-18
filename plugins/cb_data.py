import re
import os 
import math
import time
import humanize
import asyncio


from pyrogram import Client, filters, enums
from pyrogram.types import *
from pyrogram.errors import FloodWait
from config import temp
from main import User

CAPTION = os.environ.get('CAPTION')
T_CHANNEL = int(os.environ.get("T_CHANNEL", "-1001837941527"))
F_CHANNEL = int(os.environ.get("F_CHANNEL", "-1001737494519"))
R_LOG = int(os.environ.get("FF_CHANNEL", "-1001862098106"))
PROGRESS_BAR = "\n\n📁 : {b} | {c}\n🚀 : {a}%\n⚡ : {d}/s\n⏱️ : {f}"

U_CHANNEL = int(os.environ.get("U_CHANNEL", "-1001815935001"))

@User.on_message(filters.private)
async def pm_reply(bot, msg):
    a = await msg.reply_chat_action(enums.ChatAction.TYPING)
    await asyncio.sleep(0.4)
    b = await msg.reply_text("hy👀")

@User.on_message(filters.chat(U_CHANNEL) & (filters.document | filters.video))
async def autost(bot, msg):
    media = msg.document or msg.audio or msg.video
    og_media = getattr(msg, msg.media.value)
    filename = og_media.file_name
    new_name = filename
    cap = f"`{new_name}`"
    try:
       copy = await User.copy_message(F_CHANNEL, U_CHANNEL, msg.id)
    except Exception as e:
       await print(f"{e}")

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
         name = re.sub(r'\[CC\]\.*', '', filename)
         result = re.sub(r'@CC_', '', name)
         new_name = result
         file = msg.document or msg.video
         file_path = f"downloads/{new_name}"
         sts = await bot.send_message(chat_id=R_LOG, text=f"Trying to Download 📩\n\n`{new_name}`")
         c_time = time.time()
         try:
     	    path = await bot.download_media(message = file, progress=progress_message, progress_args=(f"Downloading 📩 `{new_name}`", sts, c_time))
         except Exception as e:
     	     await ms.edit(e)

         splitpath = path.split("/downloads/")
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
         await sts.edit(f"Trying to Uploading\n`{new_name}`")
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
             print("f{e}")
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
    if round(diff % 60.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)                                    
        progress = "\n{0}{1}".format(
            ''.join(["■" for i in range(math.floor(percentage / 5))]),
            ''.join(["□" for i in range(20 - math.floor(percentage / 5))]))                                  
        tmp = progress + PROGRESS_BAR.format(
            a=round(percentage, 2),
            b=humanbytes(current),
            c=humanbytes(total),
            d=humanbytes(speed),
            f=estimated_total_time if estimated_total_time != '' else "0 s")                               
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
