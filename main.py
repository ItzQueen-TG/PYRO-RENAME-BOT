from pyrogram import Client, compose, idle
from config import API_ID, API_HASH, BOT_TOKEN
from aiohttp import web
from route import web_server
from pyromod import listen

app = Client(
    "renamer",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "plugins"},
    sleep_threshold=15
)

if __name__ == "__main__":
    app.start()
    print("Bot started!")
    idle()
