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
                                   get_form_field_label('email')})
    password = PasswordField(get_form_field_label('password'),
                             render_kw={'placeholder':
                                        get_form_field_label('password')})
    remember = BooleanField(get_form_field_label('remember_me'))
    submit = SubmitField(get_form_field_label('login'))

    def __init__(self, *args, **kwargs):
        self.email.fa = 'fa-envelope-o'
        self.password.fa = 'fa-key'
        super(UsersLoginForm, self).__init__(*args, **kwargs)
