import os
from pyrogram import Client


Bot = Client(
    "Translator Bot",
    bot_token = os.getenv ["BOT_TOKEN"],
    api_id = int(os.getenv ["API_ID"]),
    api_hash = os.getenv ["API_HASH"],
    plugins = dict(root="plugins")
)


Bot.run()
