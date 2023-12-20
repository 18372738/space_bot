import datetime
import json
import os
from urllib.parse import urlparse

from environs import Env
import requests

from download_foto import save_images


def get_format_file(url):
    path = urlparse(url).path
    path_file, format_file = os.path.splitext(path)
    return format_file


def fetch_nasa_image_day():
    env = Env()
    env.read_env()
    today = datetime.date.today()
    start = datetime.date(today.year, today.month - 1, today.day)
    token = {
        'api_key': env.str('TOKEN_NASA'),
        'start_date': start,
        'end_date' : today,
    }

    response = requests.get('https://api.nasa.gov/planetary/apod/', params=token).text
    apod = json.loads(response)
    for number, url in enumerate(apod):
        print(url)
        if get_format_file(url['url']) == ".jpg":
            save_images(url['url'], f'images/nasa_apod_{number}.jpg')


if __name__ == '__main__':
  os.makedirs('images', exist_ok=True)
  fetch_nasa_image_day()
