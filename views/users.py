from db_api.users import get_all_users


async def all_users() -> str:
    """Возвращает список всех пользователей бота в виде текста"""
    users = await get_all_users()
    msg = 'Список всех пользователей бота:\n'
    msg += '\n'.join(user for user in users)
    return msg
