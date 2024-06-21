from aiogram import Router, F
from aiogram.filters import Filter, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app.database.requests import set_item

admin = Router()


class AddItem(StatesGroup):
    name = State()
    desc = State()
    price = State()
    photo = State()


class Admin(Filter):
    def __init__(self):
        self.admins = [123, 1234]

    async def __call__(self, message: Message):
        return message.from_user.id in self.admins


@admin.message(Admin(), Command('add_item'))
async def add_item(message: Message, state: FSMContext):
    await state.set_state(AddItem.name)
    await message.answer('Напишите название товара')


@admin.message(Admin(), AddItem.name)
async def add_item_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddItem.desc)
    await message.answer('Напишите описание товара')


@admin.message(Admin(), AddItem.desc)
async def add_item_desc(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(AddItem.price)
    await message.answer('Напишите цену товара')


@admin.message(Admin(), AddItem.price)
async def add_item_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(AddItem.photo)
    await message.answer('Отправьте фото товара')


@admin.message(Admin(), AddItem.photo, F.photo)
async def add_item_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await set_item(data)
    await message.answer('Товар добавлен!')
    await state.clear()
