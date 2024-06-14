#(©)CodeXBotz
#Recoded By @Its_Tartaglia_Childe



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6386749203:AAFqct8mvHnQz81uTWU5G9IM71xuQNz308M")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21310924"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fa4c3f582286d969ab1d08449e9533e8")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002040348280"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6907639205"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://itzmeproman:itzmeproman@itzmeproman.ccssik6.mongodb.net/?retryWrites=true&w=majority&appName=itzmeproman")
DB_NAME = os.environ.get("DATABASE_NAME", "itzmeproman1n")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1002199785078"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002103601712"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002014464845"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1002099352045"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {mention} 😏\n𝗧𝗵𝗶𝘀 𝗕𝗼𝘁 𝗜𝘀 𝗠𝗮𝗱𝗲 𝗙𝗼𝗿 : @Powerkami.\n\n𝗔𝗰𝗰𝗲𝘀𝘀 𝗢𝘂𝗿 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝗕𝗲𝗹𝗼𝘄 :\n\n╔═══*｡❅*⋆⍋✧ ✦ ✧⍋⋆*❅｡*═══╗\n\n📌 @Powerprime\n\n╚═══*｡❅*⋆⍋✧ ✦ ✧⍋⋆*❅｡*═══╝</b>")
try:
    ADMINS=[7030439873]
    for x in (os.environ.get("ADMINS", "5984035173 7268039061 5984035173 6666868150 6565476720 6258381233 6360741702").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

try:
    ATUL=[7030439873]
    for h in (os.environ.get("ATUL", "6907639205").split()):
        ATUL.append(int(h))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 𝐒𝐢𝐫/𝐌𝐚𝐦 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥𝐬 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐭𝐫𝐲 𝐚𝐠𝐚𝐢𝐧....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

AUTO_DELETE = int(os.environ.get("AUTO_DELETE", "10")) # Time in Minutes
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "600")) # Time in Seconds


#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "𝐏𝐥𝐞𝐚𝐬𝐞 𝐝𝐨𝐧𝐭 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐦𝐞 𝐝𝐢𝐫𝐞𝐜𝐭𝐥𝐲 𝐈 𝐜𝐚𝐧𝐭 𝐝𝐨 𝐚𝐧𝐲𝐭𝐡𝐢𝐧𝐠 𝐨𝐭𝐡𝐞𝐫 𝐭𝐡𝐚𝐧 𝐚𝐝𝐦𝐢𝐧𝐬..!"

ADMINS.append(OWNER_ID)
ADMINS.append(6376328008)

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
