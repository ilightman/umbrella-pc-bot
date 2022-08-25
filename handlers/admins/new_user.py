from aiogram import types
from aiogram.utils.deep_linking import get_start_link

from bot import dp
from db_api.users import update_job_title, get_user_by_id
from keyboards.admin_kb import speciality_cb
from misc.filters import IsAdmin


@dp.message_handler(IsAdmin(), commands=['get_start_link'])
async def get_start_link_command(message: types.Message):
    msg = await get_start_link('umbrella_pc new user', encode=True)
    await message.answer(f'Ссылка для регистрации новых сотрудников - <b>{msg}</b>')


@dp.callback_query_handler(IsAdmin(), speciality_cb.filter())
async def new_user_select_speciality(cb: types.CallbackQuery, callback_data: dict):
    await cb.answer()
    speciality, user_id = callback_data.get('title'), callback_data.get('user_id')
    if speciality == 'admin':
        await update_job_title(user_id, admin=True)
    if speciality == 'manager':
        await update_job_title(user_id, manager=True)
    if speciality == 'pc_builder':
        await update_job_title(user_id, pc_builder=True)
    if speciality == 'courier':
        await update_job_title(user_id, courier=True)
    user = await get_user_by_id(user_id)
    msg = f'Ваша должность - {user.speciality}'
    await dp.bot.send_message(chat_id=user_id, text=msg)
    await cb.message.answer(f'Должность для {user.first_name} - {user.speciality}')
