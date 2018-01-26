#! -*- coding:utf-8 -*-

from flask_admin import AdminIndexView


class CustomIndexView(AdminIndexView):

    """
        index视图
    """

    def __init__(self, *args, **kwargs):

        """ 定义初始化参数 """

        url = '/'
        template = 'index.html'
        super(CustomIndexView, self).__init__(*args, url=url,
                                              template=template, **kwargs)
