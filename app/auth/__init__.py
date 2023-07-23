from .auth import auth


def init_app(app):
    # 注册路由
    app.register_blueprint(auth)
