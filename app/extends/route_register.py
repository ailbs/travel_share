from app import api
from app import auth
from app.extends import authorization
from app.utils.response import Response
from werkzeug.exceptions import HTTPException


# 初始化路由
def init_app(app):
    # 注册路由
    api.init_app(app)
    auth.init_app(app)

    # 注册全局异常处理机制
    app.register_error_handler(404, _404)
    app.register_error_handler(Exception, _exception)

    # 注册全局函数
    app.before_request(before_request)


def before_request():
    print('__before_request execute__')
    # 执行授权认证
    authorization.request_auth()


def _404(error):
    return Response(404, '页面跑丢了~~~').build(), 404


def _exception(e):
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = Response(e.code, f"name: {e.name},description: {e.description}").build()
        response.content_type = "application/json"
        return response
    else:
        return Response().Err().message("\n".join(e.args)).build()


