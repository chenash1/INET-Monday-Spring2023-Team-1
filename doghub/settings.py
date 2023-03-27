"""
Django settings for doghub project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

if "DOGHUB_DB_ENV" in os.environ and os.environ["DOGHUB_DB_ENV"] == "DEV":
    DEBUG = True
else:
    DEBUG = False


ALLOWED_HOSTS = [
    "doghub-production-env.eba-7pbt5sqz.us-west-2.elasticbeanstalk.com",
    "127.0.0.1",
    "doghub-develop-env.eba-jymag3pg.us-west-2.elasticbeanstalk.com",
    "172.31.23.176",  # Private IPv4 addresses for AWS EC2 Develop instance
    "172.31.13.70",  # Private IPv4 addresses for AWS EC2 Prod instance
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "doghub_app",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "doghub.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "doghub_app" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
LOGIN_URL = "login"
WSGI_APPLICATION = "doghub.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# doghub_db_envs documentation:
# PROD is currently set to AWS doghub-develop-env
# LOCAL is your local mysql instance running on 127.0.0.1


if "DOGHUB_DB_ENV" in os.environ and os.environ["DOGHUB_DB_ENV"] == "PROD":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "doghub",  # database name, must exist
            "USER": os.getenv("AWS_MYSQL_DOGHUB_USERNAME"),
            "PASSWORD": os.getenv("AWS_MYSQL_DOGHUB_PWD"),
            "HOST": os.getenv("AWS_MYSQL_HOST"),
            "PORT": "3306",
        }
    }


elif "DOGHUB_DB_ENV" in os.environ and os.environ["DOGHUB_DB_ENV"] == "DEV":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "doghub_dev",  # database name, must exist
            "USER": os.getenv("AWS_MYSQL_DOGHUB_USERNAME"),
            "PASSWORD": os.getenv("AWS_MYSQL_DOGHUB_PWD"),
            "HOST": os.getenv("AWS_MYSQL_HOST"),
            "PORT": "3306",
        }
    }


elif "DOGHUB_DB_ENV" in os.environ and os.environ["DOGHUB_DB_ENV"] == "LOCAL":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "doghub",  # database name, must exist
            "USER": os.getenv("LOCAL_MYSQL_USERNAME"),
            "PASSWORD": os.getenv("LOCAL_MYSQL_PWD"),
            "HOST": "127.0.0.1",
            "PORT": "3306",
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": str(BASE_DIR / "db.sqlite3"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa: E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "doghub_app/static")]

STATIC_ROOT = os.path.join(BASE_DIR, "assets")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# a custom user class that subclass Django User
# provides more flexibility than default auth_user
AUTH_USER_MODEL = "doghub_app.CustomUser"
AUTHENTICATION_BACKENDS = [
    "doghub_app.backends.CustomAuth",
]

# configuration for uploaded images/files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# SMTP Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

BASE_URL = os.getenv("BASE_URL_DOGHUB")
