#! -*- coding:utf-8 -*-

from flask_admin import Admin

from views import CustomIndexView


class InitAdmin(Admin):

    """ 初始化flask_admin """

    def init_app(self, *args, **kwargs):

        """ 初始化admin对象 """

        # index视图
        cv = CustomIndexView()

        super(InitAdmin, self).init_app(*args, index_view=cv, **kwargs)

        # 注册视图
        self.register_view()

    def register_view(self):
        pass
