from typing import Protocol  # type: ignore

from .repository import IRepository  # type: ignore


class IService(Protocol):
    @property
    def repository1(self) -> IRepository:
        ...

    @repository1.setter
    def repository1(self) -> IRepository:
        ...

    @property
    def repository2(self) -> IRepository:
        ...

    @repository2.setter
    def repository2(self) -> IRepository:
        ...

    def say_hello(self):
        ...
