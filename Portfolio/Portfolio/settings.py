"""
Django settings for Portfolio project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
# from rest_framework import permissions
import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django-Environ configuration
env = environ.Env(
    # set casting, default value
    USE_SSL=(bool, False),
    DEBUG_MODE=(bool, False),
    SECRET_KEY=(str, 'secret-key'),
    DBNAME=(str, 'kalwak'),
    DBUSER=(str, 'postgres'),
    DBPASSWORD=(str, 'password'),
    HOST=(str, 'localhost'),
    PORT=(str, '5432'),
    LOGGING=(bool, False),  # If this is False then some tests oriented towards logs may fail.
    SENDGRID_API_KEY=(str, 'password'),
    EMAIL=(str, 'kalwakcr@gmail.com'),
    LOGS_LIMIT=(int, 10),
    FRONTEND_URL=(str, "http://localhost:5433")
)
# reading .env file
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG_MODE')
LOGGING = env('LOGGING')  # Boolean to check if logging is enabled
LOGS_LIMIT = env('LOGS_LIMIT')  # Limit the amount of logs saved to the database

# If using build (without frontend nodejs server) or in production mode, then set the environment variable to ""
FRONTEND_URL = env('FRONTEND_URL')  # This is needed to the HireUs section in frontend (service_request in backend)

SECURE_SSL_REDIRECT = env('USE_SSL')
SESSION_COOKIE_SECURE = env('USE_SSL')
CSRF_COOKIE_SECURE = env('USE_SSL')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'Blog',
    'Email',
    'Project',
    'Service',
    'frontend',
]

if DEBUG:
    INSTALLED_APPS += ['django_extensions']
    GRAPH_MODELS = {
        'all_applications': True,
        'group_models': True,
    }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Project.middleware.LoggingMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

# If CORS_ORIGIN_ALLOW_ALL is False then uncomment
"""CORS_ORIGIN_WHITELIST = (
    'http://localhost:5433',
    'http://localhost:5432',
    'http://localhost:8080',
)"""

if LOGGING:
    MIDDLEWARE += ['request_logging.middleware.LoggingMiddleware']

ROOT_URLCONF = 'Portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates/")
        ],
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

WSGI_APPLICATION = 'Portfolio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DBNAME'),
        'USER': env('DBUSER'),
        'PASSWORD': env('DBPASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True
USE_L10N = True

TIME_ZONE = 'America/Costa_Rica'

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/assets/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'assets')

# Email django SMTP configuration
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = env('SENDGRID_API_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = env('EMAIL')
SERVER_EMAIL = env('EMAIL')
ADMINS = (
    ('Me', env('EMAIL')),
)

# Logging configuration
if LOGGING:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
            'verbose': {
                'format': '{levelname} {asctime} {pathname} {funcName}' +
                          ' {process:d} {thread:d} {message}',
                'style': '{',
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
            'file_error': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'logs/errors.log'),
                'formatter': 'standard',
            },
            'file_debug': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'logs/debug.log'),
                'formatter': 'verbose',
            },
            'email_errors': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['file_error', 'email_errors'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'debugger': {
                'handlers': ['file_debug'],
                'level': 'DEBUG',
                'propagate': False,
            },
        },
    }

REQUEST_LOGGING_ENABLE_COLORIZE = False
