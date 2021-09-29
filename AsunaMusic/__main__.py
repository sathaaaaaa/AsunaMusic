import os
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from AsunaMusic.plugins import run

Bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AsunaMusic/plugins"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")



print("\n[INFO] - STARTED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")

print("\n[INFO] - STOPPED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")

Bot.start()
run()

