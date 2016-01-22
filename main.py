import os

from flask import render_template

from db import app
from db import db

from db_loader import build_sample_db


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
    app.run(debug=app.config['DEBUG'])
