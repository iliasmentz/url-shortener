from shorty.common.exceptions.validation_exception \
    import ValidationException

from shorty.shortenusecase.providers.provider_factory \
    import ProviderFactory

from shorty.shortenusecase.validators.provider_validator \
    import ProviderValidator

from shorty.shortenusecase.validators.url_validator \
    import UrlValidator


class ShortenUseCase:
    DEFAULT_PROVIDER = "bitly"

    def __init__(self, request):
        provider = self.get_requested_or_default_provider(request)
        self.provider = provider.lower()
        if 'url' not in request:
            raise ValidationException('empty-url', 'Please send a url with your request')
        self.url = request['url']
        self.link = ""

    def get_requested_or_default_provider(self, request):
        if 'provider' not in request:
            return self.DEFAULT_PROVIDER
        return request['provider']

    def execute(self):
        self.validate_request()
        provider = ProviderFactory.retrieve(self.provider)
        self.link = provider.shorten(self.url)
        return self.to_response()

    def validate_request(self):
        UrlValidator.validate(self.url)
        ProviderValidator.validate(self.provider)

    def to_response(self):
        return {
            "data": {
                "url": self.url,
                "link": self.link,
            }
        }
