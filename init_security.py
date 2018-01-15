#! -*- coding:utf-8 -*-

from flask_security import Security

from models import datastore


class InitSecurity(Security):

    """ 自定义Security类 """

    def init_app(self, app, *args, **kwargs):

        state = super(InitSecurity, self).init_app(*args,
                                                   app=app,
                                                   datastore=datastore,
                                                   register_blueprint=False,
                                                   **kwargs)
        return state


# 实例化security
sec = InitSecurity()
