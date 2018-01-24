#! -*- coding:utf-8 -*-

from flask_admin import Admin
from flask_admin.menu import MenuLink

from init_db import db
from app.models import Users
from app.views import CustomIndexView
from app.views import UsersView
from global_cont import NAME


class InitAdmin(Admin):

    """ 初始化flask_admin """

    def init_app(self, *args, **kwargs):

        """ 初始化admin对象 """

        # index视图
        cv = CustomIndexView()

        super(InitAdmin, self).init_app(*args, index_view=cv, **kwargs)

        # 注册视图
        self.register_views()

        self.register_links()

    def register_views(self):
        self.add_view(UsersView(Users, db.session))

    def register_links(self):
        self.add_link(MenuLink(name='login', endpoint='users.login'))


admin = InitAdmin(name=NAME, template_mode='bootstrap3')
