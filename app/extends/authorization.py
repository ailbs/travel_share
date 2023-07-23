from flask import request
from flask import current_app as app
from flask_jwt_extended import verify_jwt_in_request


# 免认证装饰器
def no_auth(func):
    func.authorization = False
    return func


# 请求认证
def request_auth():
    # 获取路由信息
    endpoint = None if request.endpoint is None else app.view_functions[request.endpoint]
    # 是否启用认证
    if endpoint is not None and not hasattr(endpoint, 'authorization'):
        verify_jwt_in_request()
        pass
