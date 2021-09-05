import datetime
import asyncio
from aiogram.utils.exceptions import BadRequest

import logging

from aiogram import types 

from aiogram.dispatcher.filters import Command, Text
from keyboards.inline.inline_secret_show import secret_show, inline_mode_keyboard_secret
from keyboards.inline.callback_data import secret_callbackData , inline_callbackData



from loader import dp, bot

from uuid import uuid4



#--------------------------------------------------------------------------------------------

global baza 
baza = {}

    


@dp.inline_handler()
async def secreter(query : types.InlineQuery):
	logging.info(query)
	logging.info(f"{query.from_user.username=}")
	logging.info(f"{query.from_user.full_name=}")

	if len(query.query)>200:
		await query.answer(results=[
		        	types.InlineQueryResultArticle(
		        		id=f"{uuid4()}",
		        		title=f"Xabar hajmi me'yordan oshib ketdi",
		        		input_message_content=types.InputTextMessageContent(
							message_text='.')
		        		)
		        		
					])
	else:



		if len(query.query)>10 :		
			args = query.query.split()		
			username = args.pop(0)
			username = username.replace("@", '')
			args_final = ' '.join(args)
			sender = f"{query.from_user.username}"
			global baza
			baza = {
			    	"text" : args_final,
	            	"user" : username,
	            	"sender" : sender
					}


			if baza.get('user'):

				await query.answer(results=[
			        	types.InlineQueryResultArticle(
			        		id=f"{uuid4()}",
			        		title=f"Bu xabar {baza.get('user')} uchun",
			        		input_message_content=types.InputTextMessageContent(
								message_text=f"bu xabar <a href='https://t.me/{baza.get('user')}'> {baza.get('user')} </a> uchun "),
			        		reply_markup=inline_mode_keyboard_secret,
							description=f"{baza.get('text')}")
						])
		else:
			await query.answer(results=[

				types.InlineQueryResultArticle(

					id=f"{uuid4()}",
					title="Foydalanuvchi 'username'ni va mantni kiriting ",
					input_message_content=types.InputTextMessageContent(
						message_text='.'
						)
					)
				]
				)






# #-------------------------------------------------------------------------------------

# @dp.message_handler(Command("secret"))
# async def bot_start(message: types.Message):
#     # await message.answer(f"Salom, {message.from_user.full_name}!")
#     logging.info(message)
#     logging.info(f"{message.from_user.username=}")
#     logging.info(f"{message.from_user.full_name=}")

#     text_args = message.get_args()
#     if text_args:
#         args = text_args.split()
#         username = args[0]
#         trash = args.pop(0)
#         args_final = ' '.join(args)
#         global data
#         data = {
#             "text" : args_final,
#             "user" : username
#             }
#         if data.get('user'):

#             await message.answer(f"bu xabar <a href='https://t.me/{data.get('user')}'> {data.get('user')} </a> uchun ", reply_markup=secret_show)
#             await asyncio.sleep(0.001)
#             await message.delete()
  

#         else:

#             await message.answer("bunday foydalanuvchi topilmadi")
 

# #-----------------------------callback---------------------------------------------------------------------

@dp.callback_query_handler(inline_callbackData.filter(item_name="inline_calback"))
async def show_secret(call: types.CallbackQuery, callback_data : dict):
	logging.info(call)
	logging.info(f"{call.from_user.username=}")
	logging.info(f"{call.from_user.full_name=}")
	global baza 
	if baza['user']:

		sender = baza['sender']

		username = baza['user']
		if username==call.from_user.username or sender==call.from_user.username:
			await call.answer(f"{baza['text']}" , cache_time=1, show_alert=True)
		else:
			await call.answer(f"bu xabar siz uchun emas " , cache_time=10, show_alert=True)
	else :
		await message.answer("bunday foydalanuvchi topilmadi")


