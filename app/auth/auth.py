import hashlib
from flask import request
from flask import Blueprint
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from app.models import User
from app.extends.authorization import no_auth
from app.utils.response import Response

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=('POST',))
@no_auth
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(account=username).first()
    if user:
        # 计算sha1
        sha1 = hashlib.sha1()
        sha1.update(password.encode('utf-8'))
        if user.password == sha1.hexdigest():
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            # 返回信息
            return Response()\
                .data({'access_token': access_token, 'refresh_token': refresh_token})\
                .message('登录成功')\
                .build()
        else:
            return Response.Err().message('用户账号或密码错误').build()
    else:
        return Response.Err().message('用户不存在').build()


@auth.route('/logout', methods=('GET',))
def logout():
    pass


@auth.route('/token/refresh', methods=('GET',))
@jwt_required(refresh=True)
@no_auth
def refresh_jwt():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return Response().data({'access_token': access_token}).build()
