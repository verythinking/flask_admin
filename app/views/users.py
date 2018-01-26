#! -*- coding:utf-8 -*-

from flask import after_this_request
from flask_admin import expose
from flask_admin.helpers import get_form_data, get_redirect_target
from flask_login import login_user
from flask_security.decorators import anonymous_user_required
from flask_security.views import _commit

from app.forms import UsersLoginForm
from . import SqlaView
from global_cont import LOGIN_TITLE


class UsersView(SqlaView):

    """
        用户相关视图
    """

    login_template = 'users/login.html'
    register_template = 'users/register.html'
    create_template = 'users/register.html'

    def _refresh_forms_cache(self):

        super(UsersView, self)._refresh_forms_cache()
        # 定义登录表单类
        self._login_form_class = UsersLoginForm

    def login_form(self, obj=None):

        """
           用户模型的登录form
        """

        return self._login_form_class(get_form_data(), obj=obj)

    @expose('/login/', methods=('GET', 'POST'))
    @anonymous_user_required
    def login(self):

        """
            用户登录视图
        """

        page_title = LOGIN_TITLE
        return_url = get_redirect_target() or self.get_url('.index_view')

        form = self.login_form()

        if self.validate_form(form):
            login_user(form.user, remember=form.remember.data)
            after_this_request(_commit)

        template = self.login_template

        return self.render(template,
                           form=form,
                           page_title=page_title,
                           return_url=return_url)
