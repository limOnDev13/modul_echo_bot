import asyncio
from aiogram import Dispatcher, Bot
from config_data.config import Config, export_config
from handlers import other_answer_handler, start_help_handlers


async def main():
    config: Config = export_config(path=None)

    dp: Dispatcher = Dispatcher()
    bot: Bot = Bot(token=config.tg_bot.token)

    dp.include_router(start_help_handlers.router)
    dp.include_router(other_answer_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
