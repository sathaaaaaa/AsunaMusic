import os
import requests
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE
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

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()



print("\n[INFO] - STARTED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")

print("\n[INFO] - STOPPED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")

Bot.start()
run()

