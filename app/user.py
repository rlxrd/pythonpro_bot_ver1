from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('<a href="https://youtube.com/">Добро</a> <i>пожаловать</i> в <b>интернет-магазин!</b>',
                         reply_markup=kb.main,
                         parse_mode='HTML')


@user.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите товар!',
                         reply_markup=await kb.catalog())


@user.callback_query(F.data.startswith('sneakers_'))
async def catalog_item(callback: CallbackQuery):
    await callback.answer('Вы выбрали кроссовки')
    
    # sneakers_info = [item for brand in kb.sneaker_brands for item in brand.values() if item['name'] == callback.data.split('_')[1]]
    
    # await callback.message.answer_photo(photo=sneakers_info[0]['photo'],
    #                                     caption=sneakers_info[0]['desc'])
    
    for brand in kb.sneaker_brands:
        for item in brand.values():
            if item['name'] == callback.data.split('_')[1]:
                sneakers_info = item
    
    await callback.message.answer_photo(photo=sneakers_info['photo'],
                                        caption=sneakers_info['desc'],
                                        parse_mode='HTML')


# sneakers_adidas
# [sneakers, adidas]
