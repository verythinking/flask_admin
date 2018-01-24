#! -*- coding:utf-8 -*-

from flask import Flask

from init_db import db
from init_admin import admin
from init_security import sec

app = Flask(__name__)


def create_app(conf):

    """
        初始化app
    """

    # 获取配置
    app.config.from_object(conf)

    # 初始化扩展
    admin.init_app(app)
    db.init_app(app)
    sec.init_app(app)

    return app
