from typing import Optional

from shorty.shortenusecase.providers.bitly_provider import BitlyProvider
from shorty.shortenusecase.providers.provider import Provider
from shorty.shortenusecase.providers.tinyurl_provider import TinyUrlProvider


class ProviderFactory:
    provider_mapping = {
        "bitly": BitlyProvider,
        "tinyurl": TinyUrlProvider
    }

    @classmethod
    def retrieve(cls, provider_name) -> Optional[Provider]:
        return cls.provider_mapping.get(provider_name)

    @classmethod
    def get_provider_names(cls):
        return cls.provider_mapping.keys()
