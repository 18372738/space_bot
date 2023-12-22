import datetime
import json
import os
from urllib.parse import urlparse

from environs import Env
import requests

from download_foto import save_image


def get_format_file(url):
    path = urlparse(url).path
    path_file, format_file = os.path.splitext(path)
    return format_file


def fetch_nasa_image_day(token_nasa):
    today = datetime.date.today()
    start = datetime.date(today.year, today.month - 1, today.day)
    params = {
        'api_key': token_nasa,
        'start_date': start,
        'end_date' : today,
    }

    response = requests.get('https://api.nasa.gov/planetary/apod/', params=params)
    response.raise_for_status()
    apod = response.json()
    for number, url in enumerate(apod):
        if get_format_file(url['url']) == ".jpg":
            save_image(url['url'], f'images/nasa_apod_{number}.jpg')


if __name__ == '__main__':
    env = Env()
    env.read_env()
    token_nasa = env.str('TOKEN_NASA')
    os.makedirs('images', exist_ok=True)
    fetch_nasa_image_day(token_nasa)
