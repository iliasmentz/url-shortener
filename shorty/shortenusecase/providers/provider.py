from abc import abstractmethod


class Provider:

    @staticmethod
    @abstractmethod
    def shorten(url: str) -> str:
        pass
