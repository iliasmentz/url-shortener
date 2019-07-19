class ShortyException(Exception):
    def __init__(self, status: int, code: str, detail: str):
        self.status = status
        self.code = code
        self.detail = detail

    def to_response(self):
        return {
            "error": {
                "status": self.status,
                "code": self.code,
                "detail": self.detail
            }
        }

    def get_status(self):
        return self.status
