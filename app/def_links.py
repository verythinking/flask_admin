#! -*- coding:utf-8 -*-

from views.link_list import LinkList

links = [
    {
        'name': 'login',
        'endpoint': 'users.login'
    }
]

als = LinkList()
als.addlinks(links)
