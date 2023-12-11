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
        """getting object from database by primary key

        :param pk: object Primary Key
        :return: object if exist or None
        """

    @abstractmethod
    def save(self, obj: BaseModel) -> BaseModel:
        """save object to database

        :param obj: obj detail
        :return: obj detail from database
        """

    @abstractmethod
    def update(self, pk: T, obj: BaseModel) -> BaseModel:
        """update object in database by primary key

        :param pk: object primary key
        :param obj: object new data
        :return: object detail
        """

    @abstractmethod
    def delete(self, pk: T) -> None:
        """delete object from database by primary key

        :param pk: object primary key
        """
