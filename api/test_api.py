from flask import Blueprint, jsonify
from ..models.user import User
from ..utils.db import db


api = Blueprint('api', __name__)


@api.route('/test', methods=['GET'])
def test():
    return "Hello World"


@api.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    print(user)
    return jsonify(user.to_dict())
