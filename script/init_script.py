#! -*- coding:utf-8 -*-

from flask_script import Manager, Server

from app import create_app
from config import DevelopConfig
from db_command import DataBase


app = create_app(DevelopConfig)


def create_manager():
    """
        初始化脚本对象
    """

    # 实例化manager
    manager = Manager(app)

    # 创建runserver命令
    manager.add_command('runserver', Server(port=5000, host='0.0.0.0'))

    # 添加数据库命令
    manager.add_command('database', DataBase())

    return manager
