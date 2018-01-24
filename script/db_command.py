#! -*-coding:utf-8 -*-

from flask_script import Command, Option
from init_db import db


class DataBase(Command):

    """
        初始化数据库
    """
    option_list = (
        Option('--action', '-a', dest='action'),
    )

    def run(self, action):
        if action == 'reset':
            # 先清理数据库
            db.drop_all()
            # 建立数据库表
            db.create_all()
