from aiogram import types

from bot import dp
from misc.commands_list import ADMIN_COMMANDS
from misc.filters import IsAdmin
from views.users import all_users


@dp.message_handler(IsAdmin(), commands=['all_users'])
async def all_users_command(message: types.Message):
    msg = await all_users()
    await message.answer(msg)


@dp.message_handler(IsAdmin(), commands=['help'])
async def help_command(message: types.Message):
    await message.answer(ADMIN_COMMANDS)

# @dp.message_handler(IsAdmin())
# async def start_admin(message: types.Message):
#     await message.answer('Вы админ!')
