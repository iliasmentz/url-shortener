from shorty.common.exceptions.shorty_exception import ShortyException

HTTP_STATUS = 503
ERROR_CODE = "provider-error"
DETAIL_MESSAGE = "{} is unavailable"


class ProviderException(ShortyException):

    def __init__(self, provider: str):
        self.message = DETAIL_MESSAGE.format(provider)
        super().__init__(HTTP_STATUS, ERROR_CODE, self.message)
