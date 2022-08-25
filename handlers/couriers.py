from aiogram import types

from bot import dp
from misc.commands_list import COURIER_COMMANDS
from misc.filters import IsCourier


@dp.message_handler(IsCourier(), commands=['help'])
async def help_command(message: types.Message):
    await message.answer(COURIER_COMMANDS)


@dp.message_handler(IsCourier())
async def start_courier(message: types.Message):
    await message.answer('Вы курьер!')
