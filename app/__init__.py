from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from app.models.ModeloUsuario import ModeloUsuario
from app.models.entities.Usuario import Usuario


from .models.Modelolibro import Modelolibro
from .models.ModeloUsuario import ModeloUsuario

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    print(request.method)

    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        usuario = Usuario(None, request.form['usuario'], request.form['password'], None)
        logueado = ModeloUsuario.login(db,usuario)
        if logueado:
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/libros')
def listados_libros():
    try:
        libros = Modelolibro.listar_libros(db)
        data = {
            'libros': libros
        }
        return render_template('listado_libros.html', data=data)
    except Exception as ex:
        print(ex)


def pag_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app():
    app.register_error_handler(404, pag_no_encontrada)
    csrf.init_app(app)
    return app
