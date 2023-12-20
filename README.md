# Космический телеграм

Космический телеграм - это проект, с помощью которого вы можете скачать фотографии с сайта NASA и SpaceX. Так же, с помощью телеграм бота, вы сможете отправить фотографии из деректории в телеграм чат.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Создайте файл ".env" в вашей деректории проекта откройте его в любом текстовом редакторе. Вам понадобятся следующие переменные окружения:
```
TOKEN_NASA=API-токен с сайта NASA
```
Для получения API-токена с сайта NASA перейдите [по ссылке](https://api.nasa.gov) 

```
TOKEN_TELEGRAM=API-токен телеграм бота
CHAT_ID_TELEGRAM=ID вашего телеграм чата или телеграм канала
```

Чтобы получить API-токен телеграм бота, вам понадобиться зарегестрировать бота. Как зарегестрировать [бота](https://way23.ru/регистрация-бота-в-telegram.html)?

### Пример запуска кода

Скачать фотографию дня с сайта NASA (скрипт скачивает 20-30 фотографий при запуске)
```
python get_nasa_foto.py
```


Скачать с сайта NASA EPIC-фото земли (EPIC-Earth Polychromatic Imaging Camera)
```
python get_epic_foto.py
```


Скачать фотографии с последнего запуска SpaceX
```
python fetch_spacex_images.py
```
Иногда с последнего запуска нет фотографий, тогда вам понадобиться ID запуска и запустить скрипт следующим образом. Где взять [ID запуска](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1)? 
```
python fetch_spacex_images.py --id 5eb87d47ffd86e000604b38a
```
Отправить одну фотографию в чат телеграма из деректории
```
python publishes_one_photo_telegram.py - отправляет случайную фотографию
python publishes_one_photo_telegram.py --name_file nasa_apod_9.jpg - отправяет фотографию которую укажете
```

Отправить все фотографии в чат телеграма из деректории
```
python publishes_all_photo_telegram.py
```
По умолчанию фотографии будут отправляться по очереди с интервалом 4 часа. Вы можете сами установить интервал передав значение в секундах. Пример:
```
python publishes_all_photo_telegram.py --delay 60 - интервал отправки 1 минута
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).