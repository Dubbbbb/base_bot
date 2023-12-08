from typing import Annotated

from pydantic import AfterValidator

__all__ = [
    "ListStrEnv"
]


ListStrEnv = Annotated[str | list[str], AfterValidator(func=lambda x: x.split(",") if isinstance(x, str) else x)]
