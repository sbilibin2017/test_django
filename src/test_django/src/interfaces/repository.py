from typing import Protocol  # type: ignore


class IRepository(Protocol):
    def say_hello(self) -> str:
        ...
