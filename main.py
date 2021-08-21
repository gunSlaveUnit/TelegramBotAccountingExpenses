import asyncio

from aiogram import Bot, Dispatcher

from envparser import EnvParser
from handlers import start_handler, categories_list_handler

config = EnvParser.parse()


def register_handlers(dispatcher):
    dispatcher.register_message_handler(start_handler, commands={"start", "restart"})
    dispatcher.register_message_handler(categories_list_handler, commands={"categories"})


async def main():
    bot = Bot(token=config['BOT_TOKEN'])
    try:
        dispatcher = Dispatcher(bot=bot)
        register_handlers(dispatcher)
        await dispatcher.start_polling()
    finally:
        await bot.close()


if __name__ == '__main__':
    asyncio.run(main())
