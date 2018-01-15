#! -*- coding:utf-8 -*-

from flask import Flask

from init_db import db
from init_admin import InitAdmin
from init_security import sec
from global_cont import NAME


app = Flask(__name__)

admin = InitAdmin(name=NAME, template_mode='bootstrap3')


def create_app(app, conf):

    """ 初始化app """

    # 获取配置
    app.config.from_object(conf)

    admin.init_app(app)
    db.init_app(app)
    sec.init_app(app)
    return app
