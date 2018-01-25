#! -*-coding:utf-8 -*-

from flask_admin.menu import MenuLink


class LinkList(list):

    def addlink(self, kwargs):
        self.append(MenuLink(**kwargs))

    def addlinks(self, links):
        for link in links:
            self.addlink(link)
