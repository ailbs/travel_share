import os
from flask import Flask
from app.extends import route_register
from app.utils import db,logger

__version__ = (1, 0, 0, "dev")


def create_app(test_config=None):
    # 创建flask app实例
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        # 加载默认配置文件
        app.config.from_pyfile(app.root_path + '/config.py', silent=False)

    else:
        # 加载环境配置文件
        app.config.from_mapping(test_config)

    # 初始化数据库
    db.init_app(app)
    # 初始化日志： 使用方式 app.logger.info('message')
    logger.init_app(app)

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
