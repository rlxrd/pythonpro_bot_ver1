import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.user import user
from app.admin import admin


async def main():
    bot = Bot(token='7042167885:AAHUQul0kQmWpaKL_mNIq4sHP0k5u2KR1o0',
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    
    dp.include_routers(user, admin)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    print('Starting up...')


async def shutdown(dispatcher: Dispatcher):
    print('Shutting down...')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
