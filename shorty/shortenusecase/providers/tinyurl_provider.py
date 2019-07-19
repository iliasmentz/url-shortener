import requests

from shorty.shortenusecase.providers.provider import Provider
from shorty.common.exceptions.provider_exception import ProviderException

PROVIDER_NAME = "tinyurl"

SUCCESS_CODE = 200
TINY_URL_ENDPOINT = "https://tinyurl.com/api-create.php"


class TinyUrlProvider(Provider):

    @staticmethod
    def shorten(url):
        try:
            response = requests.get(
                TINY_URL_ENDPOINT,
                dict(url=url),
                timeout=10
            )
            if response.status_code != SUCCESS_CODE:
                raise ProviderException(PROVIDER_NAME)

            return response.content.decode()

        except Exception:
            raise ProviderException(PROVIDER_NAME)
