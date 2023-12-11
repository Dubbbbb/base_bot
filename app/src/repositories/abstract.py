from abc import ABC, abstractmethod
from typing import TypeVar, Type

from pydantic import BaseModel

__all__ = [
    "AbstractRepository",
]


T = TypeVar("T")


class AbstractRepository(ABC):

    detail_schema: Type[BaseModel]

    @abstractmethod
    def get(self, pk: T) -> BaseModel | None:
        pass

    @abstractmethod
    def save(self, obj: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def update(self, pk: T, obj: BaseModel) -> BaseModel:
        pass

    @abstractmethod
    def delete(self, pk: T) -> None:
        pass
