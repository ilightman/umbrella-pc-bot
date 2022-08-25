from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def yes_no_inl_kb(prefix: str = '', with_cancel: bool = False):
    inl_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton('Да', callback_data=f'{prefix}:yes'),
            InlineKeyboardButton('Нет', callback_data=f'{prefix}:no'),
        ]
    ])
    if with_cancel:
        inl_kb.add(InlineKeyboardButton('Отмена', callback_data=f':cancel'))
    return inl_kb
