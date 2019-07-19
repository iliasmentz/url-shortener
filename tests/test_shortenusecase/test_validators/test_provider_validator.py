from shorty.shortenusecase.validators.provider_validator \
    import ProviderValidator


def test_provider_validator_with_existing_provider():
    # given
    provider = "bitly"
    # when
    result = ProviderValidator.is_valid_provider(provider)
    # then
    assert result


def test_provider_validator_with_not_existing_provider():
    # given
    provider = "facebook"
    # when
    result = ProviderValidator.is_valid_provider(provider)
    # then
    assert not result
