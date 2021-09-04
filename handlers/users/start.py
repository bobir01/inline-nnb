import datetime
import asyncio
from aiogram.utils.exceptions import BadRequest

import logging

from aiogram import types 
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from keyboards.inline.inline_secret_show import secret_show
from keyboards.inline.callback_data import secret_callbackData 
# from utils.datasecret import data


from loader import dp, bot 




@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")
    


#-------------------------------------------------------------------------------------

global data
data = {}

       

@dp.message_handler(Command("secret"))
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!")
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")

    text_args = message.get_args()
    if text_args:
        args = text_args.split()
        username = args[0]
        username = username.replace("@", '')
        trash = args.pop(0)
        args_final = ' '.join(args)
        global data
        data = {
            "text" : args_final,
            "user" : username
            }
        if data.get('user'):

            await message.answer(f"bu xabar <a href='https://t.me/{data.get('user')}'> {data.get('user')} </a> uchun ", reply_markup=secret_show)
            await asyncio.sleep(0.001)
            await message.delete()
  

        else:

            await message.answer("bunday foydalanuvchi topilmadi")
 

#-----------------------------callback---------------------------------------------------------------------

@dp.callback_query_handler(secret_callbackData.filter(item_name="secret_callback"))
async def show_secret(call: types.CallbackQuery, callback_data : dict):
    logging.info(call)
    logging.info(f"{call.from_user.username=}")
    logging.info(f"{call.from_user.full_name=}")
    global data 
    if data['user']:

        username = data['user']
        if username==call.from_user.username:
            await call.answer(f"{data['text']}" , cache_time=60, show_alert=True)
        else:
            await call.answer(f"bu xabar siz uchun emas " , cache_time=60, show_alert=True)
    else :
         await message.answer("bunday foydalanuvchi topilmadi")


