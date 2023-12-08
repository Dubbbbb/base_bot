from typing import Annotated

from pydantic import BeforeValidator

__all__ = [
    "ListStrEnv"
]


ListStrEnv = Annotated[str | list[str], BeforeValidator(func=lambda x: x.split(","))]
