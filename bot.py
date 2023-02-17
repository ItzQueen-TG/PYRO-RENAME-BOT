from pyrogram import Client, compose, idle
from config import API_ID, API_HASH, BOT_TOKEN, STRING, PORT
from aiohttp import web
from route import web_server
from main import User

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
        print("userbot started ⚡")
    idle()
    for app in apps:
        app.stop()
        print("bot Down💔")

else:
    bot=Bot()
    bot.run()
    print("bot started ⚡")
