#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>┏━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┓\n┃ Dҽʋҽʅσρҽɾ : <a href='tg://user?id={6258381233}'>ɱɾ Ⴆαɳƙαι </a>\n┃ ¢яєαтσя : <a href='tg://user?id={OWNER_ID}'> тнιѕ ℓєgєη∂ вσу </a>\n┃ Lαɳɠυαɠҽ : <code>Python3</code>\n┃ LιႦɾαɾყ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n┃ ѕσυя¢є ¢σ∂є : <a href=https://t.me/Mr_Bankaiiii>тαℓк тσ нιм</a>\n┃ мαιη ¢нαηηєℓ : <a href=https://t.me/PowerPrime>Main Channel</a>\n┃ Sυρρσɾƚ Gɾσυρ : <a href=https://t.me/Powerkami>ѕυρρσят gяσυρ</a>\n┗━━━━━•◦●◉✿ ❟❛❟ ✿◉●◦•━━━━━━┛</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/OtakuFlix_Network/4639')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
