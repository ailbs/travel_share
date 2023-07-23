from flask import Blueprint, jsonify
from ..extends.authorization import no_auth

api = Blueprint('api', __name__)


@api.route('/test', methods=['GET'])
def test():
    return "Hello World"
