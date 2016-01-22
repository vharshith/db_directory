from db import db


class DB_Listings(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    client_name = db.Column(db.String(80), unique=True)
    server = db.Column(db.String(255))
    db_name = db.Column(db.String(255))
    user_name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    service_name = db.Column(db.String(255))
    dev_group_name = db.Column(db.String(255))
    db_system = db.Column(db.String(255))

    def __str__(self):
        return self.client_name
