#! -*-coding:utf-8 -*-

""" 定义flask admin需要的视图列表 """

from def_exceptions import ViewsRelatedDBError


class ViewsList(list):
    """
        视图列表
        在使用时要首先使用setup_mysql_db方法，
        关联对应的数据库
    """

    def __init__(self):
        self.mysql_db = None

    def setup_mysql_db(self, mysql_db):
        self.mysql_db = mysql_db

    def add_mysql_db_view(self, view, **kwargs):
        if not self.mysql_db:
            raise ViewsRelatedDBError('views is not related mysqldb')
        self.append(view(session=self.mysql_db.session, **kwargs))

    def add_mysql_db_views(self, views):
        if not self.mysql_db:
            raise ViewsRelatedDBError('views is not related mysqldb')
        for view in views:
            view_class = view.pop('class')
            self.add_mysql_db_view(view_class, **view)
