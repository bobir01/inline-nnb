import io
import logging

from aiogram.types import Message , CallbackQuery
from aiogram.dispatcher.filters import Command, RegexpCommandsFilter
from keyboards.inline.inline_secret_show import secret_show
from filters.group_chat import IsGroup
from filters.admins import AdminFilter
from loader import dp , bot 
from aiogram.dispatcher import filters
import re

regx = r'^[a-z0-9_-]{3,15}$'

# @dp.callback_query_handler(callback_data="secret_callback")
@dp.message_handler(Command("secret"), IsGroup())
async def send_secret(message: Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")
    args = message.get_args()
    # msg = ''.join(args)
    msg = 'ndni'
    await message.answer(msg, reply_markup=secret_show, cache_time=60 ,show_alert=True)
    await bot.send_message(chat_id=835282186, text=msg)

       # source_message = message.reply_to_message
    # photo = source_message.photo[-1]
    # photo = await photo.download(destination=io.BytesIO())
    # input_file = types.InputFile(photo)
    # #1-usul
    # await message.chat.set_photo(photo=input_file)


# @dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
# async def set_new_title(message: types.Message):
#     source_message = message.reply_to_message
#     title = source_message.text
#     #2-usul
#     await bot.set_chat_title(message.chat.id, title=title)



# @dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
# async def set_new_description(message: types.Message):
#     source_message = message.reply_to_message
#     description = source_message.text
#     # 1-usul
#     # await bot.set_chat_description(message.chat.id, description=description)
#     # 2-usul
#     await message.chat.set_description(description=description)