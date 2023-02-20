from pyrogram import Client, compose, idle
from config import API_ID, API_HASH, BOT_TOKEN, STRING, PORT
from aiohttp import web
from route import web_server
from main import User
from plugins.cb_data import R_LOG

Bot = Client(
        "Renamer",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        workers=200,
        plugins={"root": "plugins"},
        sleep_threshold=15,
        )
       
if STRING:
    apps = [User,Bot]
    for app in apps:
        app.start()
        log = await Bot.send_message(LOG_CHANNEL, text="๏[-ิ_•ิ]๏ bot and user restarted !")
    idle()
    for app in apps:
        app.stop()
        print("bot Down💔")

else:
    bot=Bot()
    bot.run()
    log = await Bot.send_message(LOG_CHANNEL, text="๏[-ิ_•ิ]๏ bot restarted !")
