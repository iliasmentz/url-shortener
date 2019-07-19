import re

from shorty.common.exceptions.validation_exception import ValidationException


class UrlValidator:
    url_validation_exception = ValidationException(
        "invalid-url",
        "Please submit a valid URL to be shorten"
    )

    VALID_URL_REGEX = r'^(?:http|ftp)s?://'
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
    r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
    r'localhost|'
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r'(?::\d+)?'
    r'(?:/?|[/?]\S+)$'

    @classmethod
    def validate(cls, url):
        if not url:
            raise cls.url_validation_exception

        if not cls.is_valid_url(url):
            raise cls.url_validation_exception

    @classmethod
    def is_valid_url(cls, url):
        regex = re.compile(
            cls.VALID_URL_REGEX,
            re.IGNORECASE
        )
        return re.match(regex, url)
