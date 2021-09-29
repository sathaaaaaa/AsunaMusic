import os
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME

USER = Client(
    SESSION_NAME,
    API_ID,
    API_HASH
)

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
USER.run()
Bot.run()

