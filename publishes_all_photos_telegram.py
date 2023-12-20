import argparse
import os
import random
import time

import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()
    tg_token = env.str('TOKEN_TELEGRAM')
    chat_id = env.str('CHAT_ID_TELEGRAM')
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser(description="Программа высылает фото в чат с указанной задержкой")
    parser.add_argument("--delay", help="Задержка", default=14400)
    args = parser.parse_args()
    posting_time = args.delay
    while True:
        for folder, list, files in os.walk("images"):
            random.shuffle(files)
            for file in files:
                path = os.path.join(folder, file)
                bot.send_photo(chat_id=chat_id, photo=open(path, "rb"))
                time.sleep(posting_time)

if __name__ == "__main__":
    main()
