from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог'), KeyboardButton(text='Корзина')],
    [KeyboardButton(text='Поиск'), KeyboardButton(text='Контакты')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню.')


sneaker_brands = [
    {'adidas': {'photo': 'https://cdn.24.co.za/files/Cms/General/d/1875/c9d604fa43f14bc3bae27cbd5fc0b6bc.jpg',
                'desc': 'Отличный кроссовки от <b>Канье Уэста</b>',
                'price': 70,
                'name': 'adidas'}},
    {'newbalance': {'photo': 'https://photos6.spartoo.eu/photos/212/21200964/21200964_1200_A.jpg',
                     'desc': 'Супер кроссы долговечные',
                     'price': 100,
                     'name': 'newbalance'}},
    {'nike': {'photo': 'https://static.nike.com/a/images/t_PDP_1280_v1/f_auto,q_auto:eco/4f8049c6-d329-4907-905b-df905c3da623/dunk-low-retro-shoes-Q2Gtpp.png',
              'desc': 'Самые популярные',
              'price': 150,
              'name': 'nike'}}
]


async def catalog():
    keyboard = InlineKeyboardBuilder()
    for item in sneaker_brands:
        for brand in item.values():
            keyboard.add(InlineKeyboardButton(text=brand['name'],
                                            callback_data=f"sneakers_{brand['name']}"))
    return keyboard.adjust(2).as_markup()


#async def catalog_inline():
#    buttons = []
#    for item in sneaker_brands:
#        buttons.append([InlineKeyboardButton(text=item, callback_data=item)])
#    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
#    return keyboard
