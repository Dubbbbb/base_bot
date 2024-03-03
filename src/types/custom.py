from typing import Annotated

from annotated_types import Predicate
from fluent.runtime import FluentLocalization  # noqa
from pydantic import AfterValidator

__all__ = [
    "ASCIIAlphaStr",
    "ListStrEnv",
    "ListIntEnv",
    "Localization",
]

ASCIIAlphaStr = Annotated[str, Predicate(func=str.isascii), Predicate(func=str.isalpha)]
ListStrEnv = Annotated[
    str | list[str],
    AfterValidator(func=lambda x: x.split() if isinstance(x, str) else x)
]
ListIntEnv = Annotated[
    str | list[int],
    AfterValidator(func=lambda x: [int(val) for val in x.split()] if isinstance(x, str) else x)
]
Localization = FluentLocalization.format_value
