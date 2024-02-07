from db import db
from sqlalchemy.sql import func   

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.String(255), nullable=False)
    foto = db.Column(db.String(255), nullable=False)