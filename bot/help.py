from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
Kurulum
1) Bu botu gruplarınıza ekleyip adminlik veriniz 
2) asistanı grubunuza ekleyiniz
Commands
=>> Vidio Playing 🎧
- /stream : Görüntülü sohbette yayınlamak istediğiniz video linki veya dosyayı yanıtlayınız.
- /stop  : Yayını durdur
- /start :Botu başlat
- /help  :Yardım için
- /ly   : Şarkının alytazılarını al
- /song : Youtube'dan şarkı linki al
- /quote: Anime alıntısı almak için :)
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎵 destek ", url="https://t.me/flackwardev"
                    )
                ]
            ]
        )
    )    
