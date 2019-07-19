import pytest

from shorty.common.exceptions.provider_exception \
    import ProviderException
from shorty.shortenusecase.providers.bitly_provider \
    import BitlyProvider


def test_tiny_url_provider():
    # given
    url = 'https://www.valid-url.com'
    # when
    result = BitlyProvider.shorten(url)
    # then
    assert result.startswith('http://bit.ly/')


def test_tiny_url_provider_with_error():
    # given
    url = 'www.valid url.com'
    # then
    with pytest.raises(ProviderException):
        # when
        BitlyProvider.shorten(url)
