#! -*-coding:utf-8 -*-

from flask_security.forms import LoginForm, get_form_field_label
from wtforms import StringField, PasswordField, \
    SubmitField, BooleanField


class UsersLoginForm(LoginForm):

    """
        定义登陆表单
    """

    email = StringField(get_form_field_label('email'),
                        render_kw={'placeholder':
                                   'example@web.com.cn'})
    password = PasswordField(get_form_field_label('password'),
                             render_kw={'placeholder':
                                        'your password'})
    remember = BooleanField(get_form_field_label('remember_me'))
    submit = SubmitField(get_form_field_label('login'))

    fa_addon = {
        'email': 'fa-envelope-o',
        'password': 'fa-key'
    }
