from pyrogram import Client, compose, idle
from config import API_ID, API_HASH, BOT_TOKEN, STRING, PORT
from aiohttp import web
from route import web_server

User = Client(
        "test", 
        api_id=API_ID, 
        api_hash=API_HASH, 
        session_string=STRING)


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
        me = await Bot.get_me()
        print(f"{me.username} started ⚡")
    idle()
    for app in apps:
        app.stop()

else:
    bot=Bot()
    bot.run()
