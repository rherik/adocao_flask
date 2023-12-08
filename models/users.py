from db import db
from sqlalchemy.sql import func   

class Users(db.Model):
    __table__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
    password = db.Column(db.String(255), nullable=False)