import os

from flask import Flask, url_for, redirect, render_template, request, abort
import flask_admin
from flask_admin import helpers as admin_helpers
from flask_security import Security, SQLAlchemyUserDatastore

from db import app
from db import db

from db_loader import build_sample_db
from apps.admin.admin import MyModelView
from apps.admin.models import User
from apps.admin.models import Role


# Create admin
admin = flask_admin.Admin(
    app,
    'Example: Auth',
    base_template='my_master.html',
    template_mode='bootstrap3',
)

# Add model views
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(User, db.session))

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )

# Flask views
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db(app, db)

    # Start app
    app.run(debug=True)
