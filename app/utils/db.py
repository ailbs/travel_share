from flask import  g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_db():
    if 'db' not in g:
        g.db = db

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.session.close()


def init_app(app):
    db.init_app(app)
    app.teardown_appcontext(close_db)
