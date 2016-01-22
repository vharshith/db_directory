from flask_security import Security
from flask_admin import helpers as admin_helpers
from flask_security import SQLAlchemyUserDatastore

from db import app
from db import db

from apps.admin.admin import admin
from apps.admin.models import User
from apps.admin.models import Role
from apps.db_listings.models import DB_Listings

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
