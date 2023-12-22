import requests


def save_image(url, path, token=""):
  response = requests.get(url, params=token)
  response.raise_for_status()
  with open(path, 'wb') as file:
      file.write(response.content)
