from pyrogram import filters
from pyrogram.types import Message

from FallenRobot import pbot as pgram


@pgram.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        name = (
            message.text.split(None, 1)[1]
            if len(message.command) < 3
            else message.text.split(None, 1)[1].replace(" ", "%20")
        )
        m = await pgram.send_message(message.chat.id, "Wʀɪᴛɪɴɢ....")
        photo = "https://apis.xditya.me/write?text=" + name
        await pgram.send_photo(message.chat.id, photo=photo, caption="Wʀɪᴛᴛᴇɴ Bʏ ✍️ <a href='https://t.me/SmileHelp_Robot'>Sᴍɪʟᴇ</a>")         
        await m.delete()
    else:
        lol = message.reply_to_message.text
        name = lol.split(None, 0)[0].replace(" ", "%20")
        m = await pgram.send_message(message.chat.id, "Wʀɪᴛɪɴɢ....")
        photo = "https://apis.xditya.me/write?text=" + name
        await pgram.send_photo(message.chat.id, photo=photo, caption="Wʀɪᴛᴛᴇɴ Bʏ ✍️ <a href='https://t.me/SmileHelp_Robot'>Sᴍɪʟᴇ</a>")         
        await m.delete()

__mod_name__ = "WriteTool"
__command_list__ = ["write"]
__help__ = """
ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊.
❍ /write <ᴛᴇxᴛ> *:* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ. """
