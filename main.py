from pyrogram import Client
from config import API_ID, API_HASH, STRING

User = Client("test", api_id=API_ID, api_hash=API_HASH, session_string=STRING)
