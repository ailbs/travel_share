import os

from flask import Flask

from app.extends import route_register

# 基础目录
basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(test_config=None):
    # 创建flask app实例
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # 加载默认配置文件
        app.config.from_pyfile(basedir + '/config.py', silent=True)
    else:
        # 加载环境配置文件
        app.config.from_mapping(test_config)

    # 创建jwt实例
    from app.extends.jwt import jwt
    jwt.init_app(app)

    # 初始化路由
    route_register.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
