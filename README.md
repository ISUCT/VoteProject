VoteProject
===========
Для запуска проекта, необходимо создать файлик BaseProject/settings.py и добавить:

    from default_settings import *

    DEBUG = True
    DATABASES = {
        # Настройка базы данных
    }

Такого рода конфигурация требуется, для того чтобы не показывать имя пользователя и пароль в открытом репозитарии


# Стили и Bootstrap

Рядом с корневым каталогом требуется скачать и положить Bootstrap - http://twitter.github.io/bootstrap/

# Django-Registration

Для работы приложения также требуется модуль django-registration, который необходимо установить в свою систему например вот так:
`sudo pip install --upgrade django-registration`

# Создавайте ветки

Для упрощения жизни - работать необходимо в отдельных ветках
