from db import db
from sqlalchemy.sql import func   
#from sqlalchemy_imageattach.entity import Image, image_attachment

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    #foto = image_attachment('UserPicture')
