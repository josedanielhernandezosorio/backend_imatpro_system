"""
Django settings for backend_imatpro_system project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import environ

from pathlib import Path

# environment
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, 'config/app/.env.config.app.local'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

FIXTURE_DIRS = [os.path.join(BASE_DIR, 'config/fixture/')]

ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://0.0.0.0:3000',
    'http://localhost',
    'http://127.0.0.1',
    'http://0.0.0.0',
]

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # library
    'corsheaders',
    'rest_framework',

    # apps applicative
    'com.sofyntelligen.imatpro.app.model.system.equations.mathematical',
    'com.sofyntelligen.imatpro.app.backend.mathematical.catalog',
    'com.sofyntelligen.imatpro.app.backend.mathematical.character',
    'com.sofyntelligen.imatpro.app.backend.mathematical.equation',
    'com.sofyntelligen.imatpro.app.backend.mathematical.representation',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend_imatpro_system.urls'

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

WSGI_APPLICATION = 'backend_imatpro_system.wsgi.application'
ASGI_APPLICATION = 'backend_imatpro_system.asgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASS'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

# Pagignation
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'com.sofyntelligen.imatpro.app.utility.config.exception_handler.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'com.sofyntelligen.imatpro.app.utility.config.pagination.CustomLimitOffsetPagination',
    'PAGE_SIZE': 20,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ],
}

# Logs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'long': {
            'format': '%(asctime)s [%(levelname)s] %(process)s %(pathname)s %(funcName)s - No : %(lineno)s : %('
                      'message)s'
        },
        'simple': {
            'format': '%(asctime)s %(message)s'
        }
    },
    'handlers': {
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/loggers.error.log'),
            'formatter': 'long',
        },
        'info_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/loggers.info.log'),
            'formatter': 'long',
        },
    },
    'loggers': {
        'error_logger': {
            'handlers': ['error_file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'info_logger': {
            'handlers': ['info_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Mexico_City'

DATE_FORMAT = [
    "%m/%d/%Y",  # '10/25/2006'
    "%m-%d-%Y",  # '10-25-2006'
]
DATE_INPUT_FORMATS = [
    "%m/%d/%Y",  # '10/25/2006'
    "%m-%d-%Y",  # '10-25-2006'
]

DATETIME_FORMAT = [
    "%m/%d/%Y %H:%M",  # '2006/10/25 14:30'
    "%m/%d/%Y %H:%M:%S",  # '2006/10/25 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '2006/10/25 14:30:59.000200'
    "%m-%d-%Y %H:%M",  # '2006-10-25 14:30'
    "%m-%d-%Y %H:%M:%S",  # '2006-10-25 14:30:59'
    "%m-%d-%Y %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
]
DATETIME_INPUT_FORMATS = [
    "%m/%d/%Y %H:%M",  # '2006/10/25 14:30'
    "%m/%d/%Y %H:%M:%S",  # '2006/10/25 14:30:59'
    "%m/%d/%Y %H:%M:%S.%f",  # '2006/10/25 14:30:59.000200'
    "%m-%d-%Y %H:%M",  # '2006-10-25 14:30'
    "%m-%d-%Y %H:%M:%S",  # '2006-10-25 14:30:59'
    "%m-%d-%Y %H:%M:%S.%f",  # '2006-10-25 14:30:59.000200'
]

USE_I18N = True

USE_L10N = False

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
