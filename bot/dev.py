from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("info")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>merhaba {message.from_user.first_name}!
=> Bot Kurucusu
1) @burakizm



 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 destek grubu", url="https://t.me/flackwardev"
                    )
                ]
            ]
        )
    )    
