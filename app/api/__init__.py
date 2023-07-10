from .test_api import api
from .error import _404

def init_app(app):
    # 注册路由
    app.register_blueprint(api)
    # 注册全局异常处理机制
    app.register_error_handler(404, _404)
