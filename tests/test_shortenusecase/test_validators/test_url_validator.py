from shorty.shortenusecase.validators.url_validator import UrlValidator


def test_url_validator_with_valid_url():
    # given
    valid_url = "http://www.valid-url.com"
    # when
    result = UrlValidator.is_valid_url(valid_url)
    # then
    assert result


def test_url_validator_for_valid_url_with_query_params():
    # given
    valid_url = "http://www.example.com/products?id=1&page=2"
    # when
    result = UrlValidator.is_valid_url(valid_url)
    # then
    assert result


def test_url_url_without_protocol():
    # given
    invalid_url = "www.invalid-url.com"
    # when
    result = UrlValidator.is_valid_url(invalid_url)
    # then
    assert not result


def test_url_validator_with_invalid_format():
    # given
    invalid_url = "wrongformat"
    # when
    result = UrlValidator.is_valid_url(invalid_url)
    # then
    assert not result


def test_url_validator_with_invalid_protocol():
    # given
    invalid_url = "tcp://www.valid-url.com"
    # when
    result = UrlValidator.is_valid_url(invalid_url)
    # then
    assert not result


def test_url_validator_with_invalid_ip():
    # given
    invalid_url = "256.257.201.1"
    # when
    result = UrlValidator.is_valid_url(invalid_url)
    # then
    assert not result
