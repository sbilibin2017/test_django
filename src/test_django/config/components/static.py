from pathlib import Path

from .components import settings

BASE_DIR = Path(__file__).resolve().parent.parent


STATIC_URL = settings.app.static_url
STATIC_ROOT = BASE_DIR / settings.app.static_url[1:]
