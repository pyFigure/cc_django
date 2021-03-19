from config.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.get('DB_NAME'),
        'USER': env.get('DB_USERNAME'),
        'PASSWORD': env.get('DB_PASSWORD'),
        'HOST': env.get('DB_HOST'),
        'PORT': env.get('DB_PORT'),
    },
}
