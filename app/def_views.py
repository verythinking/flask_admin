#! -*-coding:utf-8 -*-

"""
    对于各种视图需要制定不同的信息，使用字典进行手动制定
    在通过admin对象引入并使用
"""

from init_db import db
from views.views_list import ViewsList

from views import UsersView

from models import Users

all_mysql_views = [
    {
        'class': UsersView,
        'model': Users,
    },
]

vsl = ViewsList()
vsl.setup_mysql_db(db)
vsl.add_mysql_db_views(all_mysql_views)
