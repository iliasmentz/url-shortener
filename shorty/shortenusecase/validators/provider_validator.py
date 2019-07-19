from shorty.common.exceptions.validation_exception import ValidationException
from shorty.shortenusecase.providers.provider_factory import ProviderFactory


class ProviderValidator:
    provider_validation_exception = ValidationException(
        "invalid-provider",
        "Please submit a valid provider to use for shortening, "
        "or leave it empty to select the default one."
    )

    @classmethod
    def validate(cls, provider):
        if not provider:
            raise cls.provider_validation_exception

        if not cls.is_valid_provider(provider):
            raise cls.provider_validation_exception

    @classmethod
    def is_valid_provider(cls, provider):
        providers = ProviderFactory.get_provider_names()
        return providers.__contains__(provider)
