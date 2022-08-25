from db_api.models import Order
from db_api.users import get_user_by_id


async def create_order(content: str, quantity: int, manager_id: int, photo_id: str = None):
    order_manager = await get_user_by_id(manager_id)
    order = await Order.create(
        content=content,
        quantity=quantity,
        order_manager=order_manager,
        photo_id=photo_id
    )
    return order
