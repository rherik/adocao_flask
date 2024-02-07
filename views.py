from flask import Blueprint, render_template, request, flash, redirect
from models import Post
from datetime import datetime
from db import db
import boto3
import uuid
from dotenv import load_dotenv
import os

ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'HEIC']

def allowed_files(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

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
    load_dotenv()
    if request.method == "POST":
        titulo = request.form.get('titulo')
        text = request.form.get('text')
        if not text:
            flash('Post não pode estar vazio', category='error')
        else:
            # INICIO DO TRATAMENTO DA IMAGEM
            uploaded_file = request.files["imagem"]
            if not allowed_files(uploaded_file.filename):
                flash("Tipo de arquivo não permitido", category='error')

            # Definição do arquivo
            new_filename = uuid.uuid4().hex + '.' + uploaded_file.filename.rsplit('.', 1)[1].lower()
            bucket_name = "arquivos-blogviralatas"
            regiao = "sa-east-1"

            s3 = boto3.client("s3", 
                            aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
                            aws_secret_access_key=os.getenv('AWS_ACCESS_KEY_SECRET'))
            # ARMAZENA A FOTO NO BALDE AWS
            s3.upload_fileobj(uploaded_file, bucket_name, new_filename)
            # FIM DO TRATAMENTO DA IMAGEM
            url_img = f"https://{bucket_name}.s3.{regiao}.amazonaws.com/{new_filename}"

            post = Post(title=titulo, 
                        text=text, 
                        date_created=datetime.now().strftime('%d/%m/%Y'),
                        foto=url_img
                        )

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
        novo_titulo = request.form.get('titulo')
        novo_texto = request.form.get('text')

        post_att.title = novo_titulo
        post_att.text = novo_texto
        post_att.date_created = datetime.now().strftime('%d/%m/%Y')

        db.session.commit()
        flash('Postagem atualizada!', category='success')
    return render_template('atualizar.html', posts=postes)

# @views.route('/cadastrar', methods=['GET', 'POST'])
# def cadastrar():
#     name = None
#     formulario = UserForm()
#     if formulario.validate_on_submit:
#         user = User.query.filter_by(name=formulario.name.data).first()
#         if formulario.name.data == None:
#             flash("Nome não pode estar vazio", category='error')
#         elif user is None:
#             user = User(name=formulario.name.data)
#             db.session.add(user)
#             db.session.commit()
#             flash("Usuário inserido com sucesso!")
#         elif formulario.name.data == user.name:
#             flash("Nome de usuário já existe", category='error')
#         name = formulario.name.data
#         formulario.name.data=""
#     our_users = User.query.order_by(User.date_added)
#     return render_template('signup.html', form=formulario, name=name, our_users=our_users)
