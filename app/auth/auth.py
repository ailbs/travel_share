from flask import request
from flask import Blueprint
from flask import jsonify

from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=('POST',))
def login():
    username = request.form['username']
    password = request.form['password']

    # 验证账号密码 TODO
    access_token = create_access_token(identity=username)
    # 保存当前用户token
    return jsonify(access_token=access_token)


@auth.route('/logout', methods=('GET',))
def logout():
    pass


@auth.route('/token/refresh', methods=('GET',))
def refresh_jwt():
    pass
