# TODO: сделать авторизацию. Пользователь заходит - все норм, но если хочет что-то сделать, пусть аторизуется

from aiogram import types

from categories import Categories

from phrases import START_PHRASE


def auth_needed(func):
    async def wrapper(message):
        if message['from']['is_bot']:
            return await message.reply("Access Denied. You are a bot", reply=False)
        if message['from']['id'] != 1562254533:
            return await message.reply("Access Denied", reply=False)
        return await func(message)
    return wrapper


@auth_needed
async def start_handler(message: types.Message):
    await message.reply(START_PHRASE, reply=False)


@auth_needed
async def categories_list_handler(message: types.Message):
    categories = Categories().categories
    await message.reply("\n".join(categories), reply=False)
