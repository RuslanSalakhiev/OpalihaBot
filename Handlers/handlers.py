from datetime import date
import emoji
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

import config
from Keyboards import keyboards as kb

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)


async def delete_message(message: types.Message):
    await message.delete()


async def main_menu_message(message: types.Message):
    await delete_message(message)
    await message.answer('Привет, это бот-домовой 17го дома Опалихи О3', reply_markup=kb.main_menu_keyboard())


async def main_menu_call(call: types.CallbackQuery):
    await delete_message(call.message)
    await call.message.answer('Привет, это бот-домовой 17го дома Опалихи О3', reply_markup=kb.main_menu_keyboard())
    await call.answer()


async def info(call: types.CallbackQuery):
    await delete_message(call.message)
    await call.message.answer('Полезная информация о доме', reply_markup=kb.info_keyboard(previous_step='main_menu'))
    await call.answer()


async def uprav(call: types.CallbackQuery):
    await delete_message(call.message)
    await call.message.answer('Об управляющей компании', reply_markup=kb.uprav_keyboard(previous_step='main_menu'))
    await call.answer()


async def chats(call: types.CallbackQuery):
    await delete_message(call.message)
    await call.message.answer('Чаты Опалихи О3', reply_markup=kb.chats_keyboard(previous_step='main_menu'))
    await call.answer()