import datetime
import os

import requests
from environs import Env

from download_foto import save_image


def get_epic_image(token_nasa):
    token = {
        'api_key': token_nasa,
    }

    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=token)
    response.raise_for_status()
    epics = response.json()
    for number, epic in enumerate(epics):
        image_date = epic['date'].split()[0]
        image_date_datetime = datetime.datetime.strptime(image_date, '%Y-%m-%d')
        format_image_date = image_date_datetime.strftime('%Y/%m/%d')
        image = epic['image']
        url = f'https://api.nasa.gov/EPIC/archive/natural/{format_image_date}/png/{image}.png'
        path = f'images/image_EPIC_{number}.png'
        save_image(url, path, token)


if __name__ == '__main__':
    env = Env()
    env.read_env()
    token_nasa = env.str('TOKEN_NASA')
    os.makedirs('images', exist_ok=True)
    get_epic_image(token_nasa)
