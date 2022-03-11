from datetime import date
import emoji
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
import logging

import config
from Handlers import handlers as hd

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)


dp.register_message_handler(hd.main_menu_initial, commands=['Start'])

dp.register_callback_query_handler(hd.info,
                            lambda call: call.data in ('info', 'navi_info'))
dp.register_callback_query_handler(hd.chats,
                            lambda call: call.data in ('chats', 'navi_chats'))
dp.register_callback_query_handler(hd.uprav,
                            lambda call: call.data in ('uprav', 'navi_uprav'))
dp.register_callback_query_handler(hd.kadastr,
                            lambda call: call.data in ('kadastr'))
dp.register_callback_query_handler(hd.main_menu,
                            lambda call: call.data in ('navi_main_menu'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

