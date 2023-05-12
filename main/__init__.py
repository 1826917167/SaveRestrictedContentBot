#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 23885559
API_HASH = "d86c310032223144ca3a89debb9cc868"
BOT_TOKEN = "5619262021:AAFHasoWJgYC9Kd7Cojvvg3ay-m6CNWyyC4"
SESSION = "BQAonidgIeWWhAKybHmWKihP_5t3Jd1TwCyZrbKpkBwfTfU-JQ6eCTNccMdLOt8h76fCxy3rgInn3it3gKHs5iATjSK1NssJbweeKd6gR5tAbGjDxoMmM3Z-riqG4ZIx-MgiOwKQ2lC5V-t3iZMnSq5pKJ3K5DScaYyo-A-zxQhjU0MwD1xtx7UOu-_OxQW44bnZjB6isKvAnsiy1mYDv9PZAZILbH2D-yxyU_HVRlanXWIrHd2xtM9gC7Gkp3aBGbiEqsinKpz34kVn5dFdEnH8VX89EKODXYvGIFCTgP4WhZiFPOyhmelOEhP3C_eleHnj27utHBy5-uziA1Mwvmw_AAAAAWtuoYkA"
FORCESUB = "xxxzzztele"
AUTH = 6097379721

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
