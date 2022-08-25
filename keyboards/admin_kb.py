from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

speciality_cb = CallbackData('speciality', 'title', 'user_id')


def select_speciality(user_id: int) -> InlineKeyboardMarkup:
    inl_kb = InlineKeyboardMarkup(row_width=2)

    inl_kb.add(
        InlineKeyboardButton('Админ', callback_data=speciality_cb.new(title='admin', user_id=user_id)),
        InlineKeyboardButton('Менеджер', callback_data=speciality_cb.new(title='manager', user_id=user_id)),
    )
    inl_kb.add(
        InlineKeyboardButton('Сборщик ПК', callback_data=speciality_cb.new(title='pc_builder', user_id=user_id)),
        InlineKeyboardButton('Курьер', callback_data=speciality_cb.new(title='courier', user_id=user_id)),
    )

    return inl_kb
