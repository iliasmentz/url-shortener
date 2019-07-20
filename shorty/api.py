from flask import Blueprint, jsonify, request

from shorty.shortenusecase.shorten_use_case import ShortenUseCase
from shorty.common.exceptions.shorty_exception import ShortyException

api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    request_data = request.get_json()
    use_case = ShortenUseCase(request_data)
    return jsonify(use_case.execute()), 200


@api.errorhandler(ShortyException)
def handle_shorty_exception(exception):
    return jsonify(exception.to_response()), exception.get_status()
