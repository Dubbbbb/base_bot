from typing import Annotated

from pydantic import AfterValidator
from fluent.runtime import FluentLocalization  # noqa

__all__ = [
    "ListStrEnv",
    "ListIntEnv",
    "Localization",
]


ListStrEnv = Annotated[
    str | list[str],
    AfterValidator(func=lambda x: x.split(",") if isinstance(x, str) else x)
]
ListIntEnv = Annotated[
    str | list[int],
    AfterValidator(func=lambda x: [int(val) for val in x.split(",")] if isinstance(x, str) else x)
]
Localization = FluentLocalization.format_value
