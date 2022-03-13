from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

import config
from Keyboards import keyboards as kb

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=config.token, parse_mode=types.ParseMode.HTML)


async def main_menu_initial(message: types.Message):
    await message.answer_photo(photo='https://disk.yandex.com/i/zjYiD66tgkzi8g',
                               caption='Привет, это бот 17го дома Опалихи О3. Здесь ты можешь найти полезную информацию по нашему дому и комплексу',
                               reply_markup=kb.main_menu_keyboard())


async def main_menu(call: types.CallbackQuery):
    await call.message.edit_caption(
        caption='Привет, это бот 17го дома Опалихи О3. Здесь ты можешь найти полезную информацию по нашему дому и комплексу',
        reply_markup=kb.main_menu_keyboard())
    await call.answer()


async def info(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Информация о доме',
                                    reply_markup=kb.info_keyboard(previous_step='main_menu'))
    await call.answer()


async def uprav(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Контакты управляющей компании:\nТел:+74993750571\nМоб:+79014004042',
                                    reply_markup=kb.navigation_only_keyboard(previous_step='main_menu'))
    await call.answer()


async def kpp(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Чат с информацией о работе КПП:\nt.me/kpp69\n\nГенератор квитанций на оплату взносов за КПП:\nhttps://qr.tsnopalihao3.ru',
                                    reply_markup=kb.navigation_only_keyboard(previous_step='main_menu'))
    await call.answer()



async def chats(call: types.CallbackQuery):
    if call.data == 'chats_1':
        message = '''
    
🔒 Проходная для вступления в чат ЖК t.me/chat_o3

🛑 НОВОСТНОЙ КАНАЛ ЖК t.me/joinchat/AAAAAETbnRgm-fcTa1fwdQ
🚧 Новостной канал КПП t.me/kpp69

🧸 Барахолка детских вещей t.me/joinchat/GpkTylYOErx4u3v-8YKThw
🛍 Барахолка личных вещей t.me/joinchat/GpkTyk_6eeUatORJ8FiS3A
🛠 Ремонтный чат t.me/repairs_O3
🧶 Мастера и мастерицы t.me/handmade_opaliha
🏡 Недвижимость О3 t.me/nedwizhka03

🚗 За рулём t.me/joinchat/F6W3UEbvc7vzUlkOv2qzJQ
🚙 Каршеринг t.me/carOpalihaO3
🚕 Попутчики t.me/joinchat/HCFQ400PRB4cjItI5k9vMg
'''
    else:
        message = '''
        
⛷🏂Лыжи/Сноуборд t.me/joinchat/HoIPFhEwMXJEpZe-JVZxBg
🎲 Настолки t.me/joinchat/HCFQ40mgDSAXq4_sbTDf2g
⚽️ Спорт t.me/joinchat/CGQiGg6CLpHEGmRUzuTrLg
🎮 Game Community t.me/joinchat/MAw6bBtsVmnoeq9sHPfPwA
🚴 ‍Велосипедисты t.me/joinchat/AubogFA2rbB-SBVJztq5Vg
🧖‍♂️🧖‍♀️Любители бани t.me/joinchat/EKstbRbOMKpR1aLwxT9NiA
🏕 Походы выходного дня t.me/joinchat/FPpw30VXOebRqADElZqbdw

🤱🏼 Мамы О3 t.me/joinchat/GpkTylDWSXJelYViP0A77g

🐱 Помощь бездомным животным t.me/joinchat/F6W3UEVM1Dnp0D9XgCfMwg
🐕 Владельцы дом. животных t.me/pets_o3

💃🏻 Свободные люди t.me/joinchat/HCFQ402vtm0l7t-XDVzZcA

🌱 ОЗЕЛЕНЕНИЕ О3 t.me/joinchat/HCFQ41RYhf9gaQitShAEEA
'''
    await call.message.edit_caption(caption=message,
                                    reply_markup=kb.chats_keyboard(previous_step='main_menu', current_step=call.data[-1]))
    await call.answer()


async def kadastr(call: types.CallbackQuery):
    await call.message.edit_caption(caption='Кадастровый номер дома: 50:11:0040203:9321\nУзнать кадастровый номер квартиры или кладовки: https://lk.rosreestr.ru/eservices/real-estate-objects-online',
                                    reply_markup=kb.navigation_only_keyboard(previous_step='info'))
    await call.answer()
