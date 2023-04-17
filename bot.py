from pyrogram import Client, compose, idle
from config import API_ID, API_HASH, BOT_TOKEN
from aiohttp import web
from route import web_server
from pyromod import listen

Bot = Client(
        "Renamer",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        workers=200,
        plugins={"root": "plugins"},
        sleep_threshold=15,
        )
       

 bot=Bot()
 bot.run()
 print("๏[-ิ_•ิ]๏ bot restarted ! ⚡")
