import os
from flask import Flask
from . import api
from .utils.db import db

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

    # 初始化路由
    api.init_app(app)
    db.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
