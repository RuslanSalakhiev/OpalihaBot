from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji


def navigation_buttons(previous_step):
    buttons = [
        InlineKeyboardButton(text=emoji.emojize(":right_arrow_curving_up:") + " В меню",
                             callback_data='navi_main_menu'),
        InlineKeyboardButton(text=emoji.emojize(":left_arrow:") + " Назад", callback_data='navi_' + previous_step),
    ]
    return buttons


def main_menu_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text="Информация о доме", callback_data="info"),
        InlineKeyboardButton(text="Управляющая компания", callback_data="uprav"),
        InlineKeyboardButton(text="Чаты Опалихи", callback_data="chats"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def info_keyboard(previous_step) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text="Кадастровый номер", callback_data="kadastr"),
        InlineKeyboardButton(text="Адрес", callback_data="address"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    keyboard.row(*navigation_buttons(previous_step))
    return keyboard


def chats_keyboard(previous_step) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text="Чат1", url="https://kadastr.ru"),
        InlineKeyboardButton(text="Чат2", url="https://kadastr.ru"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    keyboard.row(*navigation_buttons(previous_step))
    return keyboard


def uprav_keyboard(previous_step) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text="Контакты", callback_data="contacts"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    keyboard.row(*navigation_buttons(previous_step))
    return keyboard
