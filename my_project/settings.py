import os
from pathlib import Path
from dotenv import load_dotenv
import environ
from google.cloud import secretmanager
import logging

crud_logger = logging.getLogger('crud_logger')
load_dotenv()

env = environ.Env()
environ.Env.read_env()

def get_secret(key_name, fallback_env_var):
    if os.getenv("USE_GCP_SECRET_MANAGER") == "true":
        client = secretmanager.SecretManagerServiceClient()
        name = f"projects/{env('GOOGLE_CLOUD_PROJECT')}/secrets/{key_name}/versions/latest"
        response = client.access_secret_version(name=name)
        return response.payload.data.decode("UTF-8")
    return os.getenv(fallback_env_var)

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)  # Crea el directorio de logs si no existe

SECRET_KEY = get_secret("DJANGO_SECRET_KEY", "SECRET_KEY")
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
ROOT_URLCONF = 'my_project.urls'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s %(name)s - %(message)s'
        },
    },
    'handlers': {
        'crud_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/crud_actions.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'crud_logger': {
            'handlers': ['crud_file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

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
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASSWORD"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT", default="5432"),
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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
STATICFILES_DIRS = [BASE_DIR / "static"]
