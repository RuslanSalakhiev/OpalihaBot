from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji


def navigation_buttons(previous_step):
    buttons = [
        InlineKeyboardButton(text=emoji.emojize(":right_arrow_curving_up:") + " В меню",
                             callback_data='navi_main_menu'),
        InlineKeyboardButton(text=emoji.emojize(":left_arrow:") + " Назад",
                             callback_data='navi_' + previous_step),
    ]
    return buttons


def navigation_only_keyboard(previous_step):
    buttons = [
        InlineKeyboardButton(text=emoji.emojize(":right_arrow_curving_up:") + " В меню",
                             callback_data='navi_main_menu'),
        InlineKeyboardButton(text=emoji.emojize(":left_arrow:") + " Назад",
                             callback_data='navi_' + previous_step),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def main_menu_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=emoji.emojize(":police_car_light:") + " Аварийные службы", callback_data="avariya"),
        InlineKeyboardButton(text=emoji.emojize(":house:") + " Информация о доме", callback_data="info"),
        InlineKeyboardButton(text=emoji.emojize(":toolbox:") + " Управляющая компания", callback_data="uprav"),
        InlineKeyboardButton(text=emoji.emojize(":automobile:") + " КПП и авто", callback_data="kpp"),
        InlineKeyboardButton(text=emoji.emojize(":linked_paperclips:") + " Оформление документов",
                             callback_data="docs"),
        InlineKeyboardButton(text=emoji.emojize(":speaking_head:") + " Чаты Опалихи", callback_data="chats_1"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def info_keyboard(previous_step) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text="Кадастровые номера (дом,квартира)", callback_data="kadastr"),
        InlineKeyboardButton(text="Тех. план (pdf)", url="https://фонд214.рф/upload/iblock/9bd/17.pdf"),
        InlineKeyboardButton(text="Тех. информация", url="https://фонд214.рф/projects/opaliha/292/"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    keyboard.row(*navigation_buttons(previous_step))
    return keyboard


def docs_keyboard(previous_step) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text="Прописка и регистрация", callback_data="registration")
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    keyboard.row(*navigation_buttons(previous_step))
    return keyboard


def chats_keyboard(previous_step, current_step) -> InlineKeyboardMarkup:
    if current_step == '1':
        buttons = [InlineKeyboardButton(text="Дальше →",
                                        callback_data="chats_2")]
    else:
        buttons = [InlineKeyboardButton(text="← Назад",
                                        callback_data="chats_1")]
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
