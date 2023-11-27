"""
Django settings for {{ cookiecutter.project_slug }} project.

Generated by 'django-admin startproject' using Django 4.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from os import environ, path
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(path.join(BASE_DIR.parent, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environ.get("DJANGO_DEBUG", "True") == "True"

ALLOWED_HOSTS = [i for i in environ.get("DJANGO_ALLOWED_HOSTS", "").split(",") if i]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "djoser",
    "corsheaders",
    "drf_spectacular",
    "core",
    "user",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{{ cookiecutter.project_slug }}.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "{{ cookiecutter.project_slug }}.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "postgresql": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": environ.get("DJANGO_POSTGRES_HOST", "localhost"),
        "NAME": environ.get("DJANGO_POSTGRES_NAME", "postgres"),
        "USER": environ.get("DJANGO_POSTGRES_USER", "postgres"),
        "PASSWORD": environ.get("DJANGO_POSTGRES_PASSWORD", "postgres"),
        "PORT": int(environ.get("DJANGO_POSTGRES_PORT", 5432)),
    },
}
DATABASES = {"default": DATABASES[environ.get("DJANGO_DB", "sqlite")]}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOW_ALL_ORIGINS = DEBUG
CORS_ALLOWED_ORIGINS = [i for i in environ.get("CORS_ALLOWED_ORIGINS", "").split(",") if i]

AUTH_USER_MODEL = "user.User"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_METADATA_CLASS": "rest_framework.metadata.SimpleMetadata",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "PAGE_SIZE": 100,
}

# Email SMTP configuration
DEFAULT_FROM_EMAIL = environ.get("DJANGO_EMAIL_USER")
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = environ.get("DJANGO_EMAIL_HOST")
EMAIL_PORT = int(environ.get("DJANGO_EMAIL_PORT", 587))
EMAIL_HOST_USER = environ.get("DJANGO_EMAIL_USER")
EMAIL_HOST_PASSWORD = environ.get("DJANGO_EMAIL_PASSWORD")

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": "Bearer",
}

DELETE_USERNAME = False

DJOSER = {
    "HIDE_USERS": True,
    "SET_PASSWORD_RETYPE": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "LOGOUT_ON_PASSWORD_CHANGE": True,
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": environ.get(
        "DJANGO_ACTIVATION_URL", "api/v1/auth/activate/{uid}/{token}/"
    ),
    "LOGIN_FIELD": "email" if DELETE_USERNAME else "username",
    # "SERIALIZERS": {"current_user": "api.serializers.CustomUserSerializer"},
}

ACTIVATION_REDIRECT = environ.get("DJANGO_ACTIVATION_REDIRECT", "")

