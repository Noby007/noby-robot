from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, pbot, SUPPORT_CHAT


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message: Message):
    await message.reply_photo("https://graph.org/file/8c5fffc0f3dcc2274e305.jpg",
        caption=f"""**ʜᴇʏ {message.from_user.mention},

ɪ ᴀᴍ [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

**» ᴍʏ ᴏᴡɴᴇʀ : ᴍʀ.sᴍɪʟᴇ**
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝙊𝙒𝙉𝙀𝙍 🎇", user_id=OWNER_ID),
                    InlineKeyboardButton(
                        text="𝙎𝙊𝙐𝙍𝘾𝙀 🗞️",
                        url="https://t.me/GKBotz/25",
                    ),

                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
