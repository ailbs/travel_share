from flask import request

from app import api
from app import auth

from flask_jwt_extended import get_jwt_header
from flask_jwt_extended import verify_jwt_in_request


# 初始化路由
def init_app(app):
    # 注册路由
    api.init_app(app)
    auth.init_app(app)

    # 注册全局函数
    app.before_request(before_request)


def before_request():
    if request.endpoint != 'static':
        # 验证jwt
        verify_jwt_in_request()
        pass
    else:
        pass
    print('before request execute')
