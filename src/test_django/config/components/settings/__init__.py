from typing import Protocol

from pydantic import BaseModel

from .app import AppSettings
from .cache import CacheSettings
from .db import DBSettings
from .docker import DockerSettings


class ISettings(Protocol):
    @property
    def db(self) -> BaseModel:
        ...

    @db.setter
    def db(self) -> BaseModel:
        ...

    @property
    def cache(self) -> BaseModel:
        ...

    @cache.setter
    def cache(self) -> BaseModel:
        ...

    @property
    def app(self) -> BaseModel:
        ...

    @app.setter
    def app(self) -> BaseModel:
        ...

    @property
    def docker(self) -> BaseModel:
        ...

    @docker.setter
    def docker(self) -> BaseModel:
        ...


class Settings[T: ISettings]:  # type: ignore
    db: BaseModel = DBSettings()
    cache: BaseModel = CacheSettings()
    app: BaseModel = AppSettings()
    docker: BaseModel = DockerSettings()


settings: ISettings = Settings()


__all__ = [
    "settings",
]
