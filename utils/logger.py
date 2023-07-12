# utils/logger.py

import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler


def init_app(app):
    # 获取当前日期作为日志文件名的一部分
    current_date = datetime.now().strftime('%Y-%m-%d')
    log_filename = f'app_{current_date}.log'

    # 创建日志文件的轮转处理程序
    log_handler = RotatingFileHandler(log_filename, maxBytes=1024 * 1024, backupCount=5)

    # 设置日志级别
    log_handler.setLevel(logging.INFO)

    # 格式化日志记录
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(formatter)

    # 添加处理程序到日志记录器
    app.logger.addHandler(log_handler)
