import logging
import os
from datetime import datetime

from aiogram import Dispatcher, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from dotenv import load_dotenv
from tortoise import Tortoise

from misc.filters import IsAdmin, IsManager, IsPCBuilder, IsCourier

logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s:%(funcName)s:%(message)s', level=logging.INFO)

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

ADMIN = os.getenv("ADMIN")


async def admin_notify(disp: Dispatcher, key: str):
    try:
        await disp.bot.send_message(ADMIN,
                                    f'{datetime.now().strftime("%d.%m.%Y-%H:%M:%S")} '
                                    f'{"Бот запущен и готов к работе" if key == "on" else "Бот выключается"}')
        # print(f'{"Бот запущен и готов к работе" if key == "on" else "Бот выключается"}')
    except Exception as err:
        logging.exception(err)


async def set_default_commands(disp: Dispatcher):
    await disp.bot.set_my_commands([
        types.BotCommand("help", "Помощь"),
        # types.BotCommand("add_box", "Добавить ящик"),
        # types.BotCommand("all_box", "Отобразить все ящики"),
    ])


async def on_startup(disp: Dispatcher):
    # await admin_notify(disp, key='on')
    await set_default_commands(disp)
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['db_api.models']}
    )
    await Tortoise.generate_schemas()

    logging.info('Бот запущен и работает')


async def on_shutdown(disp: Dispatcher):
    # await admin_notify(disp, key='off')
    await disp.storage.close()
    await disp.storage.wait_closed()
    await Tortoise.close_connections()
    logging.info('Бот выключается')


if __name__ == '__main__':
    from handlers import dp

    dp.bind_filter(IsAdmin)
    dp.bind_filter(IsManager)
    dp.bind_filter(IsPCBuilder)
    dp.bind_filter(IsCourier)
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)

# @app.get('/test')
# async def test():
#     return {
#         'webhook_url': WEBHOOK_URL,
#         'get_webhook_method': API_TELEGRAM_URL + '/getwebhookinfo',
#         'set_webhook_link': API_TELEGRAM_URL + f'/setWebhook?url={WEBHOOK_URL}&secret_token={SECRET_TOKEN}',
#         'delete_webhook_link': API_TELEGRAM_URL + '/deleteWebhook',
#     }


# if box_id == str(user_id):
#     await cb.answer(EXAMPLE_BOXES_TEXT, show_alert=True)
#     return
# return {'text': '❌ <b>Вы не можете просматривать или редактировать чужие ящики!</b>'}
