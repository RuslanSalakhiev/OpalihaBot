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


async def main_menu_initial(message: types.Message):
    await message.answer_photo(photo='https://disk.yandex.com/i/zjYiD66tgkzi8g',caption='Привет, это бот-домовой 17го дома Опалихи О3', reply_markup=kb.main_menu_keyboard())


async def main_menu(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Привет, это бот-домовой 17го дома Опалихи О3', reply_markup=kb.main_menu_keyboard())
    await call.answer()


async def info(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Полезная информация о доме', reply_markup=kb.info_keyboard(previous_step='main_menu'))
    await call.answer()


async def uprav(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Об управляющей компании', reply_markup=kb.uprav_keyboard(previous_step='main_menu'))
    await call.answer()


async def chats(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Чаты Опалихи О3', reply_markup=kb.chats_keyboard(previous_step='main_menu'))
    await call.answer()

async def kadastr(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Кадастровый номер: 50:11:0040203:9321', reply_markup=kb.navigation_only_keyboard(previous_step='info'))
    await call.answer()

