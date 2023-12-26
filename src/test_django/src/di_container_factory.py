from src.interfaces import IRepository, IService
from src.repositories import Repository1, Repository2
from src.services import Service
from utils.di_container import DIContainer


class DIContainerFactory:
    @classmethod
    def create(cls) -> DIContainer:
        di_container = DIContainer()
        di_container.register("repository1", IRepository, Repository1)
        di_container.register("repository2", IRepository, Repository2)
        di_container.register("service", IService, Service)
        return di_container

    def resolve(self, di_container: DIContainer, dependency_name: str):
        from typing import cast

        from django.apps import apps as app
        from src.apps import SrcConfig

        app_config: SrcConfig = cast(
            SrcConfig, app.get_containing_app_config("src")
        )
        return app_config.di_container.resolve(dependency_name)
