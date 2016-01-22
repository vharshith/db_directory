import flask_admin
from flask import url_for, redirect, request, abort
from flask_admin.contrib import sqla
from flask_security import current_user

from db import app
from db import db

from apps.admin.admin import MyModelView
from apps.admin.admin import admin
from apps.db_listings.models import DB_Listings


## Create customized model view class
#class MyModelView(sqla.ModelView):
#
#    def is_accessible(self):
#        if not current_user.is_active or not current_user.is_authenticated:
#            return False
#
#        if current_user.has_role('superuser'):
#            return True
#
#        return False
#
#    def _handle_view(self, name, **kwargs):
#        """
#        Override builtin _handle_view in order to redirect users when a view is not accessible.
#        """
#        if not self.is_accessible():
#            if current_user.is_authenticated:
#                # permission denied
#                abort(403)
#            else:
#                # login
#                return redirect(url_for('security.login', next=request.url))

# Create admin
#admin = flask_admin.Admin(
#    app,
#    'Example: Auth',
#    base_template='my_master.html',
#    template_mode='bootstrap3',
#)

# Add model views
admin.add_view(MyModelView(DB_Listings, db.session))
