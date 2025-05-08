from .base import *
import os
from google.cloud import secretmanager

DEBUG = False

def access_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{env('GOOGLE_CLOUD_PROJECT')}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode("UTF-8")

SECRET_KEY = access_secret("DJANGO_SECRET_KEY")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'cloud': {
            'level': 'INFO',
            'class': 'google.cloud.logging.handlers.CloudLoggingHandler',
            'client': 'google.cloud.logging.Client',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['cloud'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
