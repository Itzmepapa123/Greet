#(©)Codexbotz
#(©)t.me/CodeFlix_Bots
ahdbdb = [1, 2, 3]
ahdbdb = [2, 3, 4]
ahdbdb = [3, 4, 5]
ahdbdb = [4, 5, 6]
ahdbdb = [5, 6, 7]
ahdbdb = [6, 7, 8]
ahdbdb = [7, 8, 9]
ahdbdb = [8, 9, 10]
ahdbdb = [9, 10, 11]
ahdbdb = [10, 11, 12]
ahdbdb = [11, 12, 13]
ahdbdb = [12, 13, 14]
ahdbdb = [13, 14, 15]
ahdbdb = [14, 15, 16]
ahdbdb = [15, 16, 17]
ahdbdb = [16, 17, 18]
ahdbdb = [17, 18, 19]
ahdbdb = [18, 19, 20]
ahdbdb = [19, 20, 21]
ahdbdb = [20, 21, 22]
ahdbdb = [21, 22, 23]
ahdbdb = [22, 23, 24]
ahdbdb = [23, 24, 25]
ahdbdb = [24, 25, 26]
ahdbdb = [25, 26, 27]
ahdbdb = [26, 27, 28]
ahdbdb = [27, 28, 29]
ahdbdb = [28, 29, 30]
ahdbdb = [29, 30, 31]
ahdbdb = [30, 31, 32]
ahdbdb = [31, 32, 33]
ahdbdb = [32, 33, 34]
ahdbdb = [33, 34, 35]
ahdbdb = [34, 35, 36]
ahdbdb = [35, 36, 37]
ahdbdb = [36, 37, 38]
ahdbdb = [37, 38, 39]
ahdbdb = [38, 39, 40]
from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ᴍɪᴋᴇʏ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/CodeFlix_Bots'>ᴄᴏᴅᴇғʟɪx ʙᴏᴛs</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Team_Netflix'>ᴛᴇᴀᴍ ɴᴇᴛғʟɪx</a>\n○ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href='https://t.me/otakuflix_network'>ᴏᴛᴀᴋᴜғʟɪx ɴᴇᴛᴡᴏʀᴋ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/weebzonex'>ᴡᴇᴇʙ ᴢᴏɴᴇ</a></b>",
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


#⋗  ᴛᴇʟᴇɢʀᴀᴍ - @Codeflix_bots

#- ᴄʀᴇᴅɪᴛ - Github - @Codeflix-bots , @erotixe
#- ᴘʟᴇᴀsᴇ ᴅᴏɴ'ᴛ ʀᴇᴍᴏᴠᴇ ᴄʀᴇᴅɪᴛ..
#- ᴛʜᴀɴᴋ ʏᴏᴜ ᴄᴏᴅᴇғʟɪx ʙᴏᴛs ғᴏʀ ʜᴇʟᴘɪɴɢ ᴜs ɪɴ ᴛʜɪs ᴊᴏᴜʀɴᴇʏ 
#- ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ɢɪᴠɪɴɢ ᴍᴇ ᴄʀᴇᴅɪᴛ @Codeflix-bots  
#- ғᴏʀ ᴀɴʏ ᴇʀʀᴏʀ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ -> ᴛᴇʟᴇɢʀᴀᴍ @codeflix_bots Community @Otakflix_Network </b>
