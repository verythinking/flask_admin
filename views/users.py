#! -*- coding:utf-8 -*-

from flask_admin import expose
from flask_admin.helpers import get_redirect_target
from flask_security.decorators import anonymous_user_required
from flask_security.forms import LoginForm

from . import SqlaView


class Users(SqlaView):

    """
        用户相关视图
    """

    def _refresh_forms_cache(self):
        super(Users, self)._refresh_forms_cache()

        # 定义登录表单类
        self._login_form_class = LoginForm

    def login_form(self, obj):
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
        return_url = get_redirect_target() or self.get_url('.index_view')

        form = self.create_form()
        if not hasattr(form, '_validated_ruleset') or not form._validated_ruleset:
            self._validate_form_instance(
                ruleset=self._form_create_rules, form=form)

        if self.validate_form(form):
            # in versions 1.1.0 and before, this returns a boolean
            # in later versions, this is the model itself
            model = self.create_model(form)
            if model:
                flash(gettext('Record was successfully created.'), 'success')
                if '_add_another' in request.form:
                    return redirect(request.url)
                elif '_continue_editing' in request.form:
                    # if we have a valid model, try to go to the edit view
                    if model is not True:
                        url = self.get_url(
                            '.edit_view', id=self.get_pk_value(model), url=return_url)
                    else:
                        url = return_url
                    return redirect(url)
                else:
                    # save button
                    return redirect(self.get_save_return_url(model, is_created=True))

        form_opts = FormOpts(widget_args=self.form_widget_args,
                             form_rules=self._form_create_rules)

        if self.create_modal and request.args.get('modal'):
            template = self.create_modal_template
        else:
            template = self.create_template

        return self.render(template,
                           form=form,
                           form_opts=form_opts,
                           return_url=return_url)
