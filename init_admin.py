#! -*- coding:utf-8 -*-

from flask_admin import Admin

from app.views import CustomIndexView
from app.def_views import vsl
from app.def_links import als
from global_cont import NAME


class InitAdmin(Admin):

    """ 初始化flask_admin """

    def init_app(self, *args, **kwargs):

        """ 初始化admin对象 """

        # index视图
        cv = CustomIndexView()

        super(InitAdmin, self).init_app(*args, index_view=cv, **kwargs)

        # 注册视图
        self.add_views(*vsl)

        # 注册链接
        self.add_links(*als)


admin = InitAdmin(name=NAME, template_mode='bootstrap3')
