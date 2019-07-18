HTTP_VALIDATION_ERROR_CODE = 422

HTTP_SUCCESS_CODE = 200

VALID_URL = "http://www.google.com"
EMPTY_URL = ""
INVALID_FORMAT = "wrongformat"
INVALID_PROTOCOL = "odbc://www.google.com"
INVALID_IP = "257.257.257.257"

VALID_PROVIDER = "bitly"
INVALID_PROVIDER = "facebook"


class TestApiFunctionality:

    def test_api_with_valid_url(self, post):
        # when we ask to shorten a valid url
        response = post(
            '/shortlinks',
            data={'url': VALID_URL, 'provider': VALID_PROVIDER}
        )

        # then
        assert response.status_code == HTTP_SUCCESS_CODE
        assert response.get_json()['data'] is not None
        assert response.get_json()['data']['url'] == VALID_URL
        assert response.get_json()['data']['link'] is not None

    def test_api_with_invalid_url_format(self, post):
        # when we ask to shorten a url with invalid format
        response = post('/shortlinks', data={'url': INVALID_FORMAT})

        # then
        assert response.status_code == HTTP_VALIDATION_ERROR_CODE
        assert response.get_json() == {
            "error": {
                "status": HTTP_VALIDATION_ERROR_CODE,
                "code": "invalid-url",
                "detail": "Please submit a valid URL to be shorten"
            }
        }

    def test_api_with_empty_url(self, post):
        # when we ask to shorten a url with invalid format
        response = post('/shortlinks', data={'url': EMPTY_URL})

        # then
        assert response.status_code == HTTP_VALIDATION_ERROR_CODE
        assert response.get_json() == {
            "error": {
                "status": HTTP_VALIDATION_ERROR_CODE,
                "code": "invalid-url",
                "detail": "Please submit a valid URL to be shorten"
            }
        }

    def test_api_with_invalid_url_protocol(self, post):
        # when we ask to shorten a url with invalid protocol
        response = post('/shortlinks', data={'url': INVALID_PROTOCOL})

        # then
        assert response.status_code == HTTP_VALIDATION_ERROR_CODE
        assert response.get_json() == {
            "error": {
                "status": HTTP_VALIDATION_ERROR_CODE,
                "code": "invalid-url",
                "detail": "Please submit a valid URL to be shorten"
            }
        }

    def test_api_with_invalid_url_ip(self, post):
        # when we ask to shorten an ip-url with invalid ip
        response = post('/shortlinks', data={'url': INVALID_IP})

        # then
        assert response.status_code == HTTP_VALIDATION_ERROR_CODE
        assert response.get_json() == {
            "error": {
                "status": HTTP_VALIDATION_ERROR_CODE,
                "code": "invalid-url",
                "detail": "Please submit a valid URL to be shorten"
            }
        }

    def test_api_with_invalid_provider(self, post):
        # when we ask to shorten an ip-url with invalid ip
        response = post(
            '/shortlinks',
            data={'url': VALID_URL, 'provider': INVALID_PROVIDER}
        )

        # then
        assert response.status_code == HTTP_VALIDATION_ERROR_CODE
        assert response.get_json() == {
            "error": {
                "status": HTTP_VALIDATION_ERROR_CODE,
                "code": "invalid-provider",
                "detail": "Please submit a valid provider to use for "
                          "shortening, or leave it empty to select "
                          "the default one."
            }
        }
