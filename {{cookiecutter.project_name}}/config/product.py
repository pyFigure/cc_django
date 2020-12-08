from config.base import *


DEBUG = False
SECRET_KEY = env.get('SECRET_KEY')

{%- if cookiecutter.use_celery.lower() == 'y' %}
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL')
{%- endif %}

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
