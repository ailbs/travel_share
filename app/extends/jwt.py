from flask_jwt_extended import JWTManager
from ..utils.response_vo import Response
from ..models import User

# jwt实例
jwt = JWTManager()


# @jwt.user_identity_loader
# def user_identity_lookup(account):
#     return account


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    account = jwt_data["sub"]
    user = User.query.filter_by(account=account).first()
    if user is not None:
        return user
    else:
        # 抛异常 TODO
        pass


# token失效
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return Response.ERR(401).message('token过期').build(), 401


# token无效
@jwt.invalid_token_loader
def invalid_token_callback(reason):
    return Response.ERR(401).message('token无效').build(), 401
