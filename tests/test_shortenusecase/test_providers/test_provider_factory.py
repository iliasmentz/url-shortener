from shorty.shortenusecase.providers.provider_factory \
    import ProviderFactory

from shorty.shortenusecase.providers.bitly_provider \
    import BitlyProvider

from shorty.shortenusecase.providers.tinyurl_provider \
    import TinyUrlProvider


def test_provider_factory_for_bitly():
    # given
    provider = "bitly"
    # when
    result = ProviderFactory.retrieve(provider)
    # then
    assert result is BitlyProvider


def test_provider_factory_for_tinyurl():
    # given
    provider = "tinyurl"
    # when
    result = ProviderFactory.retrieve(provider)
    # then
    assert result is TinyUrlProvider


def test_provider_factory_for_unkown():
    # given
    provider = "unknown"
    # when
    result = ProviderFactory.retrieve(provider)
    # then
    assert result is None
