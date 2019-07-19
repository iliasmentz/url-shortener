import pytest

from shorty.common.exceptions.provider_exception import ProviderException
from shorty.shortenusecase.providers.tinyurl_provider \
    import TinyUrlProvider


def test_tiny_url_provider():
    # given
    url = 'www.valid-url.com'
    # when
    result = TinyUrlProvider.shorten(url)
    # then
    assert result.startswith('https://tinyurl.com/')


def test_tiny_url_provider_with_error():
    # given
    url = 'www.valid url.com'
    # then
    with pytest.raises(ProviderException):
        # when
        TinyUrlProvider.shorten(url)
