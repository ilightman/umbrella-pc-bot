from datetime import datetime

from aiogram import types

from bot import dp
from db_api.users import get_all_user_by_speciality
from keyboards.admin_kb import select_speciality


def now_time() -> str:
    time = datetime.now()
    return time.strftime('%d.%m.%Y - %H:%M:%S')


async def notify_admins_about_new_user(user: types.User):
    admins = await get_all_user_by_speciality(admin=True)
    for admin in admins:
        msg = f'Новый пользователь добавлен\n\n' \
              f'{user.id} - {user.username} - {user.first_name}\n\n' \
              f'выберите его должность'
        inl_kb = select_speciality(user.id)
        await dp.bot.send_message(chat_id=admin, text=msg, reply_markup=inl_kb)


async def notify_pc_builders(text: str, photo: str = None):
    pc_builders = await get_all_user_by_speciality(pc_builder=True)
    for pc_builder in pc_builders:
        if photo:
            await dp.bot.send_photo(chat_id=pc_builder, photo=photo, caption=text)
        else:
            await dp.bot.send_message(chat_id=pc_builder, text=text)
