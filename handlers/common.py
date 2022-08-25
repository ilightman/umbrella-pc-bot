from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.deep_linking import decode_payload

from bot import dp
from db_api.users import create_user
from misc.service_messages import notify_admins_about_new_user


@dp.message_handler(CommandStart())
async def start_command(message: types.Message):
    args = message.get_args()
    payload = decode_payload(args)
    if payload == 'umbrella_pc new user':
        await create_user(message.from_user)
        await message.answer('Добро пожаловать в бот помощник umbrella pc, администратор сейчас выберет Вашу должность')
        await notify_admins_about_new_user(message.from_user)
    else:
        await message.delete()
        return


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def other_messages(message: types.Message):
    await message.delete()
