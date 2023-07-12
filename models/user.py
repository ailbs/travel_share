from ..utils.db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    mobile = db.Column(db.String, unique=True, nullable=False)
    account = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    avatar = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __int__(self, name, mobile, account, password, avatar, created_at, updated_at):
        self.name = name
        self.mobile = mobile
        self.account = account
        self.password = password
        self.avatar = avatar
        self.created_at = created_at
        self.updated_at = updated_at
        return self.id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile': self.mobile,
            'account': self.account,
            'password': self.password,
            'avatar': self.avatar,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
