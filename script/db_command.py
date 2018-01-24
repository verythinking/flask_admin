#! -*-coding:utf-8 -*-

from flask_script import Command, Option
from init_db import db


class DataBase(Command):

    """
        初始化数据库
    """
    option_list = (
        Option('--command', '-c', dest='command'),
    )

    def run(self, command):
        if command == 'reset':
            # 先清理数据库
            print 'clear db......'
            db.drop_all()
            # 建立数据库表
            print 'build db......'
            db.create_all()
