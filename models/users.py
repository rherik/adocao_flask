from db import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    # email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self):
        return f"Usuário:('{self.name}', '{self.email}')"


class UserForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
