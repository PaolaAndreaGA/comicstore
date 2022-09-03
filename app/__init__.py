from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def pag_no_encontrada(error):
    return render_template('errores/404.html'), 404


def inicializar_app():
    app.register_error_handler(404, pag_no_encontrada)
    return app
