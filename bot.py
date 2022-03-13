from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import datetime
import asyncio

import config
from Handlers import handlers as hd

storage = MemoryStorage()
bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)

dp.register_message_handler(hd.main_menu_initial, commands=['Start'])

dp.register_callback_query_handler(hd.info,
                                   lambda call: call.data in ('info', 'navi_info'))
dp.register_callback_query_handler(hd.chats,
                                   lambda call: call.data in ('chats_1','chats_2'))
dp.register_callback_query_handler(hd.uprav,
                                   lambda call: call.data in ('uprav', 'navi_uprav'))
dp.register_callback_query_handler(hd.kadastr,
                                   lambda call: call.data in ('kadastr'))
dp.register_callback_query_handler(hd.kpp,
                                   lambda call: call.data in ('kpp'))
dp.register_callback_query_handler(hd.main_menu,
                                   lambda call: call.data in ('navi_main_menu'))


async def monthly_reminder():
    while True:
        if datetime.datetime.now().strftime("%d") == '33':
            await bot.send_message(config.chat_id, 'привет, это напоминалка')
        await asyncio.sleep(86400)


async def on_startup(_):
    asyncio.create_task(monthly_reminder())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
