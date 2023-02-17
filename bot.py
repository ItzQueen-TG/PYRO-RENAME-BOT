from pyrogram import Client, compose, idle
from config import API_ID, API_HASH, BOT_TOKEN, STRING, PORT
from aiohttp import web
from route import web_server

User = Client("test", api_id=API_ID, api_hash=API_HASH, session_string=STRING)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username 
        self.force_channel = FORCE_SUB
        if FORCE_SUB:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB)                  
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")             
                self.force_channel = None
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"       
        await web.TCPSite(app, bind_address, PORT).start()     
        print(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
      

    async def stop(self, *args):
        await super().stop()      
        print("Bot Stopped")
       

if STRING:
    apps = [User,Bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
else:
    bot=Bot()
    bot.run()
