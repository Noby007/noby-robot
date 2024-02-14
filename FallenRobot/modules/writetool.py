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
        m = await pgram.send_message(message.chat.id, "Wait panra paiya")
        photo = "https://apis.xditya.me/write?text=" + name
        await pgram.send_photo(message.chat.id, photo=photo, caption="Yeluthi kuduthathu ✍️ <a href='https://t.me/nobygod'>nan than</a>")         
        await m.delete()
    else:
        lol = message.reply_to_message.text
        name = lol.split(None, 0)[0].replace(" ", "%20")
        m = await pgram.send_message(message.chat.id, "Wait panra paiya")
        photo = "https://apis.xditya.me/write?text=" + name
        await pgram.send_photo(message.chat.id, photo=photo, caption="Yeluthi kuduthathu ✍️ <a href='https://t.me/nobygod'>nan than</a>")         
        await m.delete()

__mod_name__ = "WriteTool"
__command_list__ = ["write"]
__help__ = """
ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊.
❍ /write <ᴛᴇxᴛ> *:* noby na yeluthi tharen da. """
