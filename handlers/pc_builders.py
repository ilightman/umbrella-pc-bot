from aiogram import types

from bot import dp
from misc.commands_list import PC_BUILDER_COMMANDS
from misc.filters import IsPCBuilder


@dp.message_handler(IsPCBuilder(), commands=['help'])
async def help_command(message: types.Message):
    await message.answer(PC_BUILDER_COMMANDS)


@dp.message_handler(IsPCBuilder())
async def start_pc_builder(message: types.Message):
    await message.answer('Вы сборщик ПК!')
