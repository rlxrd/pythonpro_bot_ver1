from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import DB_URL

engine = create_async_engine(url=DB_URL,
                             echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    description: Mapped[str] = mapped_column(String(1000))
    price: Mapped[int]
    photo: Mapped[str] = mapped_column(String(100))


class Image(Base):
    __tablename__ = 'images'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    item: Mapped[int] = mapped_column(ForeignKey('items.id'))
    image_url: Mapped[str] = mapped_column(String(200))


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
