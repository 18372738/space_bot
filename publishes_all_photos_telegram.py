import os

import telegram
from environs import Env



env = Env()
env.read_env()
tg_token = env.str('TOKEN_TELEGRAM')
bot = telegram.Bot(token=tg_token)
bot.send_message(chat_id=env.str('CHAT_ID_TELEGRAM'), text="Привет Бот")
