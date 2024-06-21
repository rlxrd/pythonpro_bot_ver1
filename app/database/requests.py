from app.database.models import async_session
from app.database.models import User, Item
from sqlalchemy import select, update, delete, desc


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def set_item(data):
    async with async_session() as session:
        session.add(Item(**data))
        await session.commit()


async def get_items():
    async with async_session() as session:
        return await session.scalars(select(Item))


async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))
