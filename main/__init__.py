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
BOT_TOKEN = "5911997227:AAGRgd8pJkY7vSQBMo4NWwNiuf0qNFa0614"
SESSION = "BQBPkprkT4LDrspOEhVC5XpE4TPk_-3deDZGfELC3RAIdUIkePQlYd2zsj4746-QWo4e1r-WM1CcdInhP55bbCqo4IuJWAtgaNmdBN6Om-vINh-9EPOyNmKG9cQ_W-p-nCi2UnYBz2xF6U4Bf0SdcvNQsiQ6WNCz16Rv8GWy6yQv3H2iLFW7X_RXTXNi1tKWh_ird8AyYviqnSfD69ETIj29cBZF3ithmTiBhU1wZV7OeXoaJOKYZ1qEVb1yu5lQq8eMbllANXSemaiVqZYNGHe0ykF2EDIvicuhLrxkBk5OFKneRoAG9z5Y0ak_2tw_n9q_9HCQ-YRS8j2wW_Fo4DCjAAAAAXUn0yEA"
FORCESUB = "DownloadPrivacyXiaZai"
AUTH = 6260511521

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
