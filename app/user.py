from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from app.states import Reg
import app.keyboards as kb

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('<a href="https://youtube.com/">Добро</a> <i>пожаловать</i> в <b>интернет-магазин!</b>',
                         reply_markup=kb.main,
                         parse_mode='HTML')
    await state.clear()


@user.message(F.text == 'Регистрация')
async def reg_name(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Введите Ваше имя.')


@user.message(Reg.name)
async def reg_number(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Отправьте Ваш контакт',
                         reply_markup=kb.send_contant)


@user.message(Reg.number, F.contact)
async def reg_ava(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    await state.set_state(Reg.ava)
    await message.answer('Отправьте картинку (аватарку)',
                         reply_markup=ReplyKeyboardRemove())


@user.message(Reg.number)
async def reg_ava_error(message: Message):
    await message.answer('Отправьте контакт правильно')


@user.message(Reg.ava, F.photo)
async def reg_done(message: Message, state: FSMContext):
    data = await state.get_data()
    await message.answer_photo(photo=message.photo[-1].file_id,
                               caption=f'Имя: {data['name']}\nНомер: {data['number']}')
    await state.clear()


@user.message(Reg.ava)
async def reg_done_error(message: Message, state: FSMContext):
    await message.answer('Отправьте ФОТО правильно')


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
