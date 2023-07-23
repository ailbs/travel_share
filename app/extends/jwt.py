from flask import jsonify

from flask_jwt_extended import JWTManager

# jwt实例
jwt = JWTManager()


@jwt.user_identity_loader
def user_identity_lookup(user):
    return 1


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return 2


# token失效
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(code="401", err="token已过期"), 401


# token无效
@jwt.invalid_token_loader
def invalid_token_callback(reason):
    return jsonify(code="401", err="token无效"), 401
