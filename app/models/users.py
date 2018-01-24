#! -*- coding:utf-8 -*-

from flask_security import UserMixin
from flask_security.utils import encrypt_password
from . import db


class Users(db.Model, UserMixin):

    """ 用户模型 """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    telphone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    active = db.Column(db.Boolean)
