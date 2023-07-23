JSON_AS_ASCII = False
JSONIFY_MIMETYPE = 'application/json;charset=utf-8'
JWT_SECRET_KEY = '12345678'
JWT_REQUIRED_DEFAULT = True
# DB configuration
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:8889/travel_share'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True  # 启用调试模式
SECRET_KEY='dev'