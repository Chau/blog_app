# -*- coding:utf-8 -*-


from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'dbuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
        }
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'app-emails')

DEFAULT_FROM_EMAIL = 'vercha@mail.ru'