from pyrogram import Client as Bot
from pyrogram import idle
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN


bot = Bot(
    ":memory:",
    API_ID,19366438
    API_HASH,ca9016cb12a69e5a311b1ae661da2fb0
    bot_token=BOT_TOKEN,5530874114:AAEkLn3CbvrRz7O9fgWNUvBRjmwKrn9YsD0
    plugins=dict(root="handlers")
)

bot.start()
run()
idle()
