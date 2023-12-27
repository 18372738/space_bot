import argparse
import os
import random

import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()
    tg_token = env.str('TOKEN_TELEGRAM')
    chat_id = env.str('CHAT_ID_TELEGRAM')
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser(description="Программа высылает указанное фото в чат")
    parser.add_argument("--filename", help="Имя файла" )
    args = parser.parse_args()
    filename = args.filename
    if not filename:
        filename = random.choice(os.listdir('images'))
    with open(f'images/{filename}', "rb") as file:
        bot.send_photo(chat_id=chat_id, photo=file)


if __name__ == "__main__":
    main()
