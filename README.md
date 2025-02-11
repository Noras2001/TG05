# Чат-бот для рекомендаций фильмов на базе Aiogram

Этот репозиторий содержит код для чат-бота, который использует библиотеку `aiogram` для получения случайных фильмов из IMDb Top 100 и предоставления информации о них пользователям.

## Описание

Чат-бот позволяет пользователю получать случайные фильмы из IMDb Top 100, с названием, годом выпуска, описанием и изображением (если оно доступно). Бот использует API IMDb для получения данных о фильмах.

### Основные функции

- **Получение случайного фильма**: Пользователь может запросить случайный фильм с помощью команды `/movie`.
- **Информация о фильме**: Бот отображает название фильма, год выпуска и описание. Также, если доступно, бот покажет изображение фильма.
- **API IMDb**: Для получения данных о фильмах используется API IMDb Top 100.

## Как запустить

1. Установите все необходимые зависимости:
   ```bash
   pip install aiogram requests
   ```

2. Создайте файл `config.py` с вашим токеном:
   ```python
   TOKEN = "your-bot-token-here"
   ```

3. Замените `"x-rapidapi-key"` в коде на ваш ключ API с [RapidAPI](https://rapidapi.com/), чтобы бот мог получать данные о фильмах из IMDb.

4. Запустите бота:
   ```bash
   python bot.py
   ```

5. Бот начнёт работать, и вы сможете взаимодействовать с ним в Telegram.

## Структура проекта

- **bot.py**: Основной файл, содержащий логику бота.
- **config.py**: Файл с конфигурацией (токен бота).
- **API IMDb**: Для получения данных используется API IMDb через RapidAPI.

## Пример взаимодействия с ботом

1. Пользователь отправляет команду `/movie`.
2. Бот отвечает с случайным фильмом, отображая название, год выпуска и описание. Если доступно изображение, оно также будет отправлено.

Пример ответа:

```
Заголовок фильма - 2023
Описание фильма
```

Или с изображением:

```
Заголовок фильма - 2023
Описание фильма [Изображение фильма]
```

## Лицензия

Этот проект лицензируется на условиях MIT.
