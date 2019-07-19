from shorty.common.exceptions.validation_exception import ValidationException


def test_validation_exception_to_response():
    # given
    code = "invalid-code"
    detail_message = "This is invalid"
    exception = ValidationException(code, detail_message)
    # when
    response = exception.to_response()
    # then
    assert response == {
        'error': {
            'status': 422,
            'code': code,
            'detail': detail_message
        }
    }
