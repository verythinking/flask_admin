# -*- coding:utf-8 -*-

from flask_script import Manager, Server

from app import create_app, app
from config import DevelopConfig


app_inst = create_app(app, DevelopConfig)

# 实例化manager
manager = Manager(app_inst)

# 创建runserver命令
manager.add_command('runserver', Server(port=5000, host='0.0.0.0'))

if __name__ == '__main__':
    manager.run()
