from flask_jwt_extended import JWTManager
from app.utils.response import Response
from app.models import User

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
    return Response.Err().message('token expire').build(), 401


# token无效
@jwt.invalid_token_loader
def invalid_token_callback(reason):
    return Response.Err().message(reason).build(), 401


@jwt.unauthorized_loader
def unauthorized_token_callback(reason):
    return Response.Err().message(reason).build(), 401
