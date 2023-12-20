import os

import telegram
from environs import Env



env = Env()
env.read_env()
tg_token = env.str('TOKEN_TELEGRAM')
bot = telegram.Bot(token=tg_token)
path = "images/nasa_apod_9.jpg"
bot.send_photo(chat_id=env.str('CHAT_ID_TELEGRAM'), photo=open(path, 'rb'))
