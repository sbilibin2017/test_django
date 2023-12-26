from functools import wraps  # type: ignore
from inspect import signature  # type: ignore
from typing import Parameter  # type: ignore
from typing import Callable

from .dtos.registration import Interface  # type: ignore
from .dtos.registration import RegistrationDTO  # type: ignore
from .dtos.registration import Implementation, RegistrationKey
from .utils.validate_signature import validate_signature  # type: ignore


class DIContainer:
    __deps: dict[RegistrationKey, RegistrationDTO] = {}

    @validate_signature
    def register(
        self,
        name: RegistrationKey,
        interface: Interface,
        implementation: Implementation,
    ) -> None:
        setattr(
            self.__deps,
            name,
            RegistrationDTO(
                interface=interface,
                implementation=implementation,
            ),
        )

    def resolve(self, name: str) -> Implementation:
        dep_implementation = self._get_dependency_implementation(name)
        self._get_dependency_interface(name)
        subdeps_interface: dict[
            RegistrationKey, Interface
        ] = self._get_subdependencies_interface(dep_implementation)
        subdeps_implementation: dict[RegistrationKey, Implementation] = {}
        if subdeps_interface is not None:
            for name, interface in subdeps_interface.items():
                subdep_implementation = self.resolve(name)
                subdeps_implementation[name] = subdep_implementation
        return dep_implementation(**subdeps_implementation)

    def _get_dependency_implementation(
        self, name: RegistrationKey
    ) -> Implementation:
        return getattr(self.__deps.get(name), "implementation")

    def _get_dependency_interface(self, name: RegistrationKey) -> Interface:
        return getattr(self.__deps.get(name), "interface")

    def _get_subdependencies_interface(
        self, implementation: Implementation
    ) -> dict:
        return getattr(signature(implementation), "parameters")

    @property  # type: ignore
    def dependencies(self) -> list[RegistrationKey]:  # type: ignore
        return list(self.__deps.keys())


def inject(container: DIContainer):
    def inner(func: Callable):
        annotations = func.__annotations__
        parameters = signature(func).parameters
        dependencies_name = container.dependencies

        @wraps(func)
        def wrapper(*args, **kwargs):
            for name, param in parameters.items():
                if (
                    (name in annotations)
                    and (name not in kwargs)
                    and (name in dependencies_name)
                ):
                    kwargs[name] = container.resolve(name)
            return func(*args, **kwargs)

        return wrapper

    return inner
