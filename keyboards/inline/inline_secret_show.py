from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# from . import secret_callbackData
from keyboards.inline.callback_data import secret_callbackData 

# # 1-usul.
# secret_show = InlineKeyboardMarkup(
#     inline_keyboard=[
#     [
#         InlineKeyboardButton(text="💻 Kurslar", callback_data="courses")
#     [
#     ]
# )


secret_show = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Show message", callback_data=secret_callbackData.new(item_name="secret_callback"))
    ]
])