import argparse
import os

import requests

from download_foto import save_images


def fetch_spacex_last_launch(spacex_launch_id):
  url = f'https://api.spacexdata.com/v5/launches/{spacex_launch_id}'
  if spacex_launch_id is None:
      url = 'https://api.spacexdata.com/v5/launches/latest'
  response = requests.get(url)
  response.raise_for_status()
  url_image = response.json()['links']['flickr']['original']
  for number, url in enumerate(url_image):
      save_images(url, f'images/spacex_{number}.jpg')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description="Программа скачивает фото по указанному ID запуска"
  )
    parser.add_argument("--id", help="ID запуска")
    args = parser.parse_args()
    spacex_launch_id = args.id
    os.makedirs('images', exist_ok=True)
    fetch_spacex_last_launch(spacex_launch_id)