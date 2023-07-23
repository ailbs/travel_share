import hashlib
from flask import request
from flask import Blueprint
from flask_jwt_extended import create_access_token
from ..models import User
from ..extends.authorization import no_auth
from ..utils.response_vo import Response

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
            # 保存当前用户token
            return Response.OK().data({'access_token': access_token}).build()
        else:
            return Response.ERR().message('用户账号或密码错误').build()
    else:
        return Response(200, '用户不存在').build()


@auth.route('/logout', methods=('GET',))
def logout():
    pass


@auth.route('/token/refresh', methods=('GET',))
def refresh_jwt():
    pass
