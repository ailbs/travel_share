from .test_api import api


def init_app(app):
    # 注册路由
    app.register_blueprint(api)
