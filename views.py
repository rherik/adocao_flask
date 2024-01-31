from flask import Blueprint, render_template, request, flash, redirect
from models import Post, User, UserForm
from datetime import datetime
from db import db

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/inicio", methods=['GET', 'POST'])
def home():
    return render_template("inicio.html")

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
        foto = request.form.get('image')
        if not text:
            flash('Post não pode estar vazio', category='error')
        elif not foto:
            flash('Insira uma foto', category='error')
        else:
            post = Post(text=text, date_created=datetime.now().strftime('%d/%m/%Y'), foto=foto)
            db.session.add(post)
            db.session.commit()
            flash('Postagem criada!', category='success')
            return redirect('/historias')
    return render_template('criar_post.html')

@views.route("/deletar", methods=['GET', 'POST'])
def deletar():
    postes = Post.query.all()
    if request.method == "POST":
        post_id = request.form.get('post_id')
        detet_post = Post.query.get_or_404(post_id)
        db.session.delete(detet_post)
        db.session.commit()
        flash('Postagem deletada!', category='success')
        return redirect('/deletar')
    return render_template('deletar.html', posts=postes)

@views.route('/atualizar', methods=['GET', 'POST'])
def atualizar():
    postes = Post.query.all()
    if request.method == "POST":
        post_id = request.form.get('post_id')
        post_att = Post.query.get_or_404(post_id)
        novo_texto = request.form.get('text')
        print(post_id, type(post_id), novo_texto, type(novo_texto))

        post_att.text = novo_texto
        post_att.date_created = datetime.now().strftime('%d/%m/%Y')

        db.session.commit()
        flash('Postagem atualizada!', category='success')
    return render_template('atualizar.html', posts=postes)

@views.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    name = None
    formulario = UserForm()
    if formulario.validate_on_submit:
        user = User.query.filter_by(name=formulario.name.data).first()
        if formulario.name.data == None:
            flash("Nome não pode estar vazio", category='error')
        elif user is None:
            user = User(name=formulario.name.data)
            db.session.add(user)
            db.session.commit()
            flash("Usuário inserido com sucesso!")
        elif formulario.name.data == user.name:
            flash("Nome de usuário já existe", category='error')
        name = formulario.name.data
        formulario.name.data=""
    our_users = User.query.order_by(User.date_added)
    return render_template('signup.html', form=formulario, name=name, our_users=our_users)
