# TODO: сделать авторизацию. Пользователь заходит - все норм, но если хочет что-то сделать, пусть аторизуется

from aiogram import types

from db import DBClient
from envparser import EnvParser
from phrases import START_PHRASE


config = EnvParser.parse()
client = DBClient(database=config['DB_NAME'],
                  user=config['DB_USER'], password=config['DB_PASS'],
                  host=config['DB_HOST'], port=config['DB_PORT'])


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
    categories = client.fetchall('*', table='category')
    await message.reply(categories, reply=False)
