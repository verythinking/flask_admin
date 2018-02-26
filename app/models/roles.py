#! -*- coding:utf-8 -*-

from . import db


class Roles(db.Model):

    """ 角色模型 """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    description = db.Column(db.String(255))

    db.relationship('Users', backref='role', lazy="dynamic")
