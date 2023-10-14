from flask import Blueprint, render_template, request, flash
from db import db
from models import Post
from datetime import datetime

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home", methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route("/historias", methods=['GET'])
def historia():
    postes = Post.query.all()
    return render_template("historias.html", posts=postes)

@views.route('/posts_div', methods=['GET'])
def retorna_posts():
    postes = Post.query.all()
    return render_template('posts_div.html', posts=postes)

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
    return render_template('criar_post.html')

@views.route("/deletar", methods=['GET', 'POST'])
def deletar():
    postes = Post.query.all()
    if request.method == "POST":
        post_id = request.form.get('post_id')
        print(post_id, type(post_id))
        detet_post = Post.query.filter_by(id=int(post_id)).first()
        db.session.delete(detet_post)
        db.session.commit()
        flash('Postagem deletada!', category='success')
    return render_template('deletar.html', posts=postes)

@views.route('/atualizar', methods=['GET', 'POST'])
def atualizar():
    postes = Post.query.all()
    if request.method == "POST":
        post_id = request.form.get('post_id')
        post_att = Post.query.filter_by(id=int(post_id)).first()
        novo_texto = request.form.get('text')
        print(post_id, type(post_id), novo_texto, type(novo_texto))

        post_att.text = novo_texto
        post_att.date_created = datetime.now()

        db.session.commit()
        flash('Postagem atualizada!', category='success')
    return render_template('atualizar.html', posts=postes)
