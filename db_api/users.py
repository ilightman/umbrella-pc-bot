from aiogram import types

from db_api.models import User


async def create_user(user: types.User) -> User:
    """Создаёт или возвращает существующий объект пользователя"""
    db_user, is_created = await User.get_or_create(
        id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    )
    return db_user


async def get_user_by_id(user_id: str | int) -> User:
    """Возвращает объект пользователя с указанным user_id"""
    user = await User.filter(id=user_id).first()
    return user


async def get_all_user_by_speciality(**kwargs):
    """Получает из базы список id пользователей, отфильтрованные по нужному параметру"""
    users = await User.filter(**kwargs)
    return tuple(user.id for user in users)


async def get_all_users():
    """Возвращает всех зарегистрированных в боте пользователей"""
    users = await User.all()
    return tuple(user for user in users)


async def update_job_title(user_id: int,
                           admin: bool = False,
                           manager: bool = False,
                           pc_builder: bool = False,
                           courier: bool = False):
    """Обновляет специальность пользователя"""
    user = await get_user_by_id(user_id)
    if admin:
        user.admin = True
    if manager:
        user.manager = True
    if pc_builder:
        user.pc_builder = True
    if courier:
        user.courier = True
    await user.save()
    return
