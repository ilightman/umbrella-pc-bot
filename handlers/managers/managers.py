from aiogram import types

from bot import dp
from misc.commands_list import MANAGER_COMMANDS
from misc.filters import IsManager


@dp.message_handler(IsManager(), commands=['help'])
async def help_command(message: types.Message):
    await message.answer(MANAGER_COMMANDS)


# @dp.message_handler(IsManager())
# async def start_manager(message: types.Message):
#     await message.answer('Вы менеджер!')
