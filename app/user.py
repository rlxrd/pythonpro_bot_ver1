from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.states import Reg
import app.keyboards as kb
import app.database.requests as rq

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await rq.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в интернет-магазин!',
                         reply_markup=kb.main,
                         parse_mode='HTML')
    await state.clear()


@user.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите товар', reply_markup=await kb.all_items())


@user.callback_query(F.data.startswith('item_'))
async def catalog_item(callback: CallbackQuery):
    item_info = await rq.get_item(callback.data.split('_')[1])
    await callback.answer(f'Вы выбрали товар {item_info.name}')
    await callback.message.answer_photo(photo=item_info.photo,
                                        caption=f'{item_info.name}\n\n{item_info.description}\n\n{item_info.price}')
