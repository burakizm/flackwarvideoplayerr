from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Merhaba!Ben telegram sesli sohbetlerinde videoları görüntülü bir şekilde yayınlayabilen botum. \n\n**yardım için /help To komutlar için:-** __ \n1) Type /info kurucu`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Dev", url="https://t.me/burakizm")
                                    ]]
                            ))
   else:
      await m.reply("****")
