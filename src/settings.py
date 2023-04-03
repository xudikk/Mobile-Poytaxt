#  Xudikk  2023/3/29.
#
#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan


"""
settings for src project.
Django 4.1.7.

"""

from pathlib import Path
import os

import dj_database_url
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

APP_NAME = "Poytaxt Mobile"


load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 1)
DEBUG = os.getenv('DEBUG', True)
ALLOWED_HOSTS = ['*'] if DEBUG else os.getenv('ALLOWED_HOSTS').split(',')

AUTH_USER_MODEL = 'api.User'

# Unauth methods
METHODS = os.getenv('AUTH_METHODS', '').split(',')


# Applications

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # internal
    'api',

    # external
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Whitenoise
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'src.wsgi.application'


# Database
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASS'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': int(os.getenv('DB_PORT')),
        }
    }
    db_from_env = dj_database_url.config(conn_max_age=600)
    DATABASES['default'].update(db_from_env)


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Media files (docs, Images, files)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Cors
# CORS_ALLOWED_ORIGINS = [
#     os.getenv('CORS_URL')
# ]
#
# CSRF_TRUSTED_ORIGINS = [
#     os.getenv('CORS_URL')
# ]
#
# CORS_ORIGIN_WHITELIST = [
#     os.getenv('CORS_URL')
# ]

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGS_DIR = BASE_DIR / 'log'


EXTERNAL_TOKENS = {
    "sms": os.getenv('SMS_TOKEN')
}

EXTERNAL_URLS = {
    "sms": os.getenv('SMS_URL')
}


RANGE = int(os.getenv('RANGE', 5))

CUSTOM_HASHING = os.getenv("HASHING")
UNHASH = os.getenv("UNHASH")

