from typing import Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import update, delete
from sqlalchemy.orm import sessionmaker, Session

from .abstract import AbstractRepository
from ..database import Base

__all__ = [
    "SQLAlchemyRepository",
]


T = TypeVar("T")


class SQLAlchemyRepository(AbstractRepository):

    model: Type[Base]

    def __init__(self, session_maker: sessionmaker) -> None:
        self.session_maker = session_maker

    def get(self, pk: T) -> BaseModel:
        with self.session_maker() as session:  # type: Session
            obj = session.get(entity=self.model, ident=pk)
            if obj is not None:
                return self.detail_schema.model_validate(obj=obj)

    def save(self, obj: BaseModel) -> BaseModel:
        instance = self.model(**obj.model_dump())
        with self.session_maker() as session:  # type: Session
            session.add(instance=instance)
            session.commit()
            return self.detail_schema.model_validate(obj=instance)

    def update(self, pk: T, obj: BaseModel) -> BaseModel:
        with self.session_maker() as session:
            session.execute(
                statement=update(self.model)
                .values(**obj.model_dump(exclude_none=True, exclude_defaults=True, exclude_unset=True))
                .filter_by(pk=pk)
            )
            session.commit()
            instance = session.get(entity=self.model, ident=pk)
            return self.detail_schema.model_validate(obj=instance)

    def delete(self, pk: T) -> None:
        with self.session_maker() as session:  # type: Session
            session.execute(
                statement=delete(self.model)
                .filter_by(pk=pk)
            )
            session.commit()
