import requests

from shorty.common.exceptions.provider_exception import ProviderException
from shorty.shortenusecase.providers.provider import Provider

PROVIDER_NAME = "bitly"

ENDPOINT = 'https://api-ssl.bitly.com/v3/shorten'

ACCESS_TOKEN = "ec79ef4d181fd0e2781d41cdadc79a439a0f8f75"


class BitlyProvider(Provider):

    @staticmethod
    def shorten(url):
        try:
            response = requests.get(
                ENDPOINT,
                dict(longUrl=url, access_token=ACCESS_TOKEN),
                timeout=10
            )
            if response.status_code != 200:
                raise ProviderException(PROVIDER_NAME)

            return response.json()['data']['url']

        except Exception:
            raise ProviderException(PROVIDER_NAME)
