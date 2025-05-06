import os
from pathlib import Path
from dotenv import load_dotenv
import environ
from google.cloud import secretmanager

def access_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{env('GOOGLE_CLOUD_PROJECT')}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=name)

    secret_data = response.payload.data.decode("UTF-8")
    return secret_data

env = environ.Env()
environ.Env.read_env()

load_dotenv()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
SECRET_KEY = env('SECRET_KEY')
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}

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

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # or adjust the path as needed
]
