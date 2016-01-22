from db import db
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

## Create admin
#admin = flask_admin.Admin(
#    app,
#    'Example: Auth',
#    base_template='my_master.html',
#    template_mode='bootstrap3',
#)
#
## Add model views
#admin.add_view(MyModelView(Role, db.session))
#admin.add_view(MyModelView(User, db.session))
#
## define a context processor for merging flask-admin's template context into the
## flask-security views.
#@security.context_processor
#def security_context_processor():
#    return dict(
#        admin_base_template=admin.base_template,
#        admin_view=admin.index_view,
#        h=admin_helpers,
#    )


