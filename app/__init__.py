from crypt import methods
from urllib.request import Request
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods = ['GET','POST'])
def login():
    
    print(request.method)

    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        return 'OK'
    else:
        return render_template('auth/login.html')


def pag_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app():
    app.register_error_handler(404, pag_no_encontrada)
    return app
