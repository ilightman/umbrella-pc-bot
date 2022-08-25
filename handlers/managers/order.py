from aiogram import types
from aiogram.dispatcher import FSMContext

from bot import dp
from keyboards.manager_kb import yes_no_inl_kb
from misc.filters import IsManager
from misc.service_messages import notify_pc_builders, now_time


@dp.message_handler(IsManager(), commands=['create_order'])
async def create_order(message: types.Message, state: FSMContext):
    await message.answer('Пришлите фото или введите конфигурацию оборудования')
    await state.set_state('photo_or_name_input')


@dp.message_handler(IsManager(), content_types=types.ContentTypes.PHOTO, state='photo_or_name_input')
async def input_photo_state(message: types.Message, state: FSMContext):
    image = ''
    if message.content_type == 'photo':
        image = message.photo[-1].file_id
    elif message.content_type == 'document':
        image = message.document.file_id
    await message.answer_photo(photo=image)
    await state.update_data(photo_id=image)
    await message.answer('Введите название товара или конфигурацию оборудования')
    await state.set_state('photo_or_name_input')


@dp.message_handler(IsManager(), content_types=types.ContentTypes.TEXT, state='photo_or_name_input')
async def input_name_state(message: types.Message, state: FSMContext):
    name = message.text
    if name.startswith('/'):
        await message.delete()
        return
    msg = f'<b>{name}</b>\n\nВведите количество'
    state_data = await state.get_data()
    photo = state_data.get('photo_id')
    if photo:
        await message.answer_photo(photo, caption=msg)
    else:
        await message.answer(msg)
    await state.update_data(name=name)
    await state.set_state('quantity_input')


@dp.message_handler(IsManager(), state='quantity_input')
async def quantity_input_state(message: types.Message, state: FSMContext):
    quantity = message.text
    state_data = await state.get_data()
    name = state_data.get('name')
    msg = f'<b>{name}</b> - <b>{quantity} шт.</b>'
    state_data = await state.get_data()
    photo = state_data.get('photo_id')
    if photo:
        await message.answer_photo(photo, caption=msg)
    else:
        await message.answer(msg)
    await message.answer('Отправить информацию сборщикам?', reply_markup=yes_no_inl_kb('send_to_pc_builders'))
    await state.update_data(quantity=quantity)
    await state.set_state('send_to_pc_builders')


@dp.callback_query_handler(IsManager(), state='send_to_pc_builders')
async def add_photo_callback(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    cb_data = cb.data.split(':')
    if cb_data[0] == 'send_to_pc_builders':
        if cb_data[1] == 'yes':
            state_data = await state.get_data()
            photo = state_data.get('photo_id')
            name, quantity = state_data.get('name'), state_data.get('quantity')
            msg = f'{now_time()} Заказ на сборку:\n\n <b>{name}</b> - <b>{quantity} шт.</b>'
            await cb.message.answer('[ да ]')
            await cb.message.answer('Заказ передан сборщикам')
            await notify_pc_builders(text=msg, photo=photo if photo else None)
    if 'no' in cb_data[1] or 'cancel' in cb_data[1]:
        await cb.message.answer('[ отмена ]')
    await cb.message.delete()
    await state.reset_state(with_data=True)
