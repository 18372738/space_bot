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
    parser.add_argument("--name_file", help="Имя файла" )
    args = parser.parse_args()
    name_files = args.name_file
    if name_files is None:
        name_files = random.choice(os.listdir('images'))
    bot.send_photo(chat_id=chat_id, photo=open(f'images/{name_files}', "rb"))

if __name__ == "__main__":
    main()
