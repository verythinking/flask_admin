#! -*- coding:utf-8 -*-

from flask_security import UserMixin
from . import db


class Users(db.Model, UserMixin):

    """ 用户模型 """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    telephone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    active = db.Column(db.Boolean)
