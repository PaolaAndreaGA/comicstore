from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

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
        print(request.form['username'])
        print(request.form['password'])
        if request.form['username'] == 'admin1' and request.form['password'] == 'admin010':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


def pag_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app():
    app.register_error_handler(404, pag_no_encontrada)
    csrf.init_app(app)
    return app
