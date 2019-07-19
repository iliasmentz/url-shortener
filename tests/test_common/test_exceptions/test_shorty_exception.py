from shorty.common.exceptions.shorty_exception import ShortyException


def test_shorty_exception_to_response():
    # given
    status = 666
    code = "invalid-code"
    detail_message = "This is invalid"
    exception = ShortyException(status, code, detail_message)
    # when
    response = exception.to_response()
    # then
    assert response == {
        'error': {
            'status': status,
            'code': code,
            'detail': detail_message
        }
    }
