#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=24266722, cast=int)
API_HASH = config("API_HASH", default=5dd6bedd030fd733bb5997a1d62a9b2a)
BOT_TOKEN = config("BOT_TOKEN", default=6372604535:AAHrSOJ2wo0WWYtKfvL89YvOabPRWMweTF4)
SESSION = config("SESSION", default=BQFyR-IAKbZtMTRmxXnPhspDjxrqbPnH9zO896u4aUeFhRP9bIcapeeL-hx5T8uBDgTvfDEx03c1DDelQ-CODLkQBvBqvNCmxW1eJlyMsBr17BJvMk4r5Pz-vUn_Ev9KJhMUk-8L17KYS0s4GI72dIAxYLFXilMBHBgTnlaS7gwTgkFPy_FSfH7yU8u2QLQRdbhVzkkSwqLY0eZlHIGkdQuCNDYaxLM4-baQQPe5YGwiZYl0GA4T01SqLKJaiqEZDtd3cO9UEdy_wItrPsPScgzMM3VOA80fbHH9SDI0WKnP4sPQ6VoqSz3n_Z93R2lvQexnlhmeA4MFf3OQZZ85b8tnvQjbFwAAAAF71jp3AQ)
FORCESUB = config("FORCESUB", default=Binarypaidleaker)
AUTH = config("AUTH", default=5091918803, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=6372604535:AAHrSOJ2wo0WWYtKfvL89YvOabPRWMweTF4,
    api_id=int(24266722),
    api_hash=5dd6bedd030fd733bb5997a1d62a9b2a
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
