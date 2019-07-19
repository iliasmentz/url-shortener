from shorty.common.exceptions.provider_exception import ProviderException


def test_provider_exception_to_response():
    # given
    exception = ProviderException("bitly")
    # when
    response = exception.to_response()
    # then
    assert response == {
        'error': {
            'status': 503,
            'code': 'provider-error',
            'detail': 'bitly is unavailable'
        }
    }
