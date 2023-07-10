import os

from flask import Flask
from .app import api


def create_app(test_config=None):
    # 创建flask app实例
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # 基础目录
    basedir = os.path.abspath(os.path.dirname(__file__))

    if test_config is None:
        # 加载默认配置文件
        app.config.from_pyfile('config.py', silent=True)
    else:
        # 加载环境配置文件
        app.config.from_mapping(test_config)

    # 初始化路由
    api.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
