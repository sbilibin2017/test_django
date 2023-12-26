from .components import settings

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": settings.db.db,
        "USER": settings.db.user,
        "PASSWORD": settings.db.password,
        "HOST": settings.docker.db_host,
        "PORT": settings.db.port,
        "ATOMIC_REQUESTS": True,
        "OPTIONS": {
            "options": "-c search_path=public,{schema}".format(
                schema=settings.db.schema_name
            )
        },
    }
}
