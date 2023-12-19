import datetime
import os

import requests
from environs import Env

from download_foto import save_images


def get_epic_image():
    env = Env()
    env.read_env()
    token = {
        'api_key': env.str('TOKEN_NASA'),
    }

    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=token)
    epics = response.json()
    for number, epic in enumerate(epics):
        data = epic['date'].split()[0]
        data = datetime.datetime.strptime(data, '%Y-%m-%d')
        data = data.strftime('%Y/%m/%d')
        image = epic['image']
        url = f'https://api.nasa.gov/EPIC/archive/natural/{data}/png/{image}.png'
        response = requests.get(url, params=token)
        url =response.url
        path = f'images/image_EPIC_{number}.png'
        save_images(url, path)


if __name__ == '__main__':
  os.makedirs('images', exist_ok=True)
  get_epic_image()
