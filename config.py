#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6700290832:AAGz22aZSWuyde8W1i813nqdYFSYHMTApT0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23539392"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5ee767ace3c694a4fb39cdd2cc78eaca")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002048004827"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Welexa")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1576425650"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://heeradevi817100:heeradevi817100@cluster0.qtwv4mb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001913585535"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002021004168"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention} 😏\n𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗜𝘀 𝗠𝗮𝗱𝗲 𝗙𝗼𝗿 : @Animex_Hyper\n\n𝗔𝗰𝗰𝗲𝘀𝘀 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝗕𝗲𝗹𝗼𝘄 :\n\n╔═══*｡❅*⋆⍋✧ ✦ ✧⍋⋆*❅｡*═══╗\n\n📌 @Animex_Hyper\n@Ongoing_Hyper\n\n╚═══*｡❅*⋆⍋✧ ✦ ✧⍋⋆*❅｡*═══╝</b>")
ADMINS = [1576425650]
try:
    for x in os.environ.get("ADMINS", "1576425650 1576425650").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")
#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @OtakuFlix_Network</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
