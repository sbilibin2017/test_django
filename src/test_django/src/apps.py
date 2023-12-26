from django.apps import AppConfig
from utils.di_container import DIContainer


class SrcConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "src"
    di_container: DIContainer

    def ready(self) -> None:
        from src.di_container_factory import DIContainerFactory

        self.di_container: DIContainer = DIContainerFactory.create()
