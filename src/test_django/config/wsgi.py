import os  # type: ignore

from django.core.wsgi import get_wsgi_application  # type: ignore

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
