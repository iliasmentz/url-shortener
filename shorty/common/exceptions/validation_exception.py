from shorty.common.exceptions.shorty_exception import ShortyException

HTTP_STATUS = 422


class ValidationException(ShortyException):

    def __init__(self, code: str, detail: str):
        super().__init__(HTTP_STATUS, code, detail)
