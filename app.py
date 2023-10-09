from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv

import os
from db import db
from views import views

def create_app(db_url=None):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '1234'
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///database.db")
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(views)

    with app.app_context():
        db.create_all()

    return app
