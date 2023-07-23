from app import api
from app import auth
from ..extends import authorization

# 初始化路由
def init_app(app):
    # 注册路由
    api.init_app(app)
    auth.init_app(app)

    # 注册全局函数
    app.before_request(before_request)


def before_request():
    print('__before_request execute__')
    # 执行授权认证
    authorization.request_auth()

