from aiogram import Dispatcher

from .group_chat import IsGroup
from loader import dp
from .admins import AdminFilter

from .private_chat import IsPrivate


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)