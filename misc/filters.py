from aiogram import types
from aiogram.dispatcher.filters import Filter

from db_api.users import get_all_user_by_speciality


class IsAdmin(Filter):
    key = 'is_admin'

    async def check(self, message: types.Message):
        return message.from_user.id in await get_all_user_by_speciality(admin=True)


class IsManager(Filter):
    key = 'is_manager'

    async def check(self, message: types.Message):
        return message.from_user.id in await get_all_user_by_speciality(manager=True)


class IsPCBuilder(Filter):
    key = 'is_pc_builder'

    async def check(self, message: types.Message):
        return message.from_user.id in await get_all_user_by_speciality(pc_builder=True)


class IsCourier(Filter):
    key = 'is_courier'

    async def check(self, message: types.Message):
        return message.from_user.id in await get_all_user_by_speciality(courier=True)
