from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/test', methods=['GET'])
def test():
    return "Hello World"
