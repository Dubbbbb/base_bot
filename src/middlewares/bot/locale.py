from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery, Message
from fluent.runtime import FluentLocalization, FluentResourceLoader  # noqa

from src import settings

__all__ = [
    "L10N",
    "L10NMiddleware"
]


class L10N(object):
    """fluent.runtime manager"""

    def __init__(
            self,
            locales: list[str],
            default_locale: str,
            resource_ids: list[str],
            roots: str | list[str],
    ) -> None:
        """init

        :param locales: allowed locales
        :param default_locale: default locale
        :param resource_ids: file names
        :param roots: path to locale folder
        """
        self.default_locale = default_locale
        self.loader = FluentResourceLoader(roots=roots)
        self.localizations = {
            locale: FluentLocalization(
                locales=[locale, self.default_locale],
                resource_ids=resource_ids,
                resource_loader=self.loader
            )
            for locale in locales
        }

    def get(self, locale: str) -> FluentLocalization:
        """getting fluent by user locale

        :param locale: user locale
        :return: FluentLocalization object
        """
        if locale in self.localizations:
            return self.localizations.get(locale)
        return self.localizations.get(self.default_locale)

    def __getitem__(self, item: str) -> FluentLocalization:
        """getting fluent by user locale

        :param item: user locale
        :return: FluentLocalization object
        """
        return self.get(locale=item)


class L10NMiddleware(BaseMiddleware):
    """localization middleware"""

    def __init__(self, l10n: L10N) -> None:
        """init

        :param l10n: L10N object
        """
        self.l10n = l10n

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        """implementation of the FluentLocalization according to the language of the user in handlers"""
        user_locale = event.from_user.language_code or settings.DEFAULT_LOCALE
        data["_"] = self.l10n.get(locale=user_locale).format_value
        return await handler(event, data)
