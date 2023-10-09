from flask import Blueprint, render_template, request, flash
from db import db
from models import Post

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route("/history", methods=['GET', 'POST'])
def historia():
    return render_template("historias.html")


@views.route("/crie", methods=['GET', 'POST'])
def create_post():
    if request.method == "POST":
        text = request.form.get('text')
        if not text:
            flash('Post não pode estar vazio', category='error')
        else:
            post = Post(text=text)
            db.session.add(post)
            db.session.commit()
            flash('Postagem criada!', category='success')
       
    return render_template('create_post.html')