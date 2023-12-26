from .components import settings

SECRET_KEY = settings.app.secret_key
DEBUG = settings.app.debug
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
