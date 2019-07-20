import pytest

from shorty.common.exceptions.validation_exception \
    import ValidationException

from shorty.shortenusecase.shorten_use_case \
    import ShortenUseCase


def test_shorten_use_case_happy_path():
    # given
    request_data = {"url": "https://www.google.gr", "provider": "bitly"}
    # when
    response = ShortenUseCase(request_data).execute()
    # then
    assert response['data']['link'].startswith("http://bit.ly")


def test_shorten_use_case_for_validation():
    # given
    request_data = {"url": "https.google.gr", "provider": "bitly"}
    with pytest.raises(ValidationException):
        # when
        ShortenUseCase(request_data).execute()
