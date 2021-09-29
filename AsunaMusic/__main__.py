import os
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from AsunaMusic.plugins.nopm import User

Bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AsunaMusic/plugins"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")

User.start()
Bot.start()
print("\n[INFO] - STARTED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")
idle()
print("\n[INFO] - STOPPED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")
User.stop()
Bot.stop()

