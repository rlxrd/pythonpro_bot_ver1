from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from app.database.requests import get_items


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'), KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Поиск'), KeyboardButton(text='Контакты')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')


async def all_items():
    keyboard = InlineKeyboardBuilder()
    items = await get_items()
    
    for item in items:
        keyboard.add(InlineKeyboardButton(text=item.name, callback_data=f'item_{item.id}'))
    
    return keyboard.adjust(1).as_markup()
