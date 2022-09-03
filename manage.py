from xmlrpc.client import Server
from flask_script import Manager, Server
from app import inicializar_app
from config import config

app = inicializar_app()

manager = Manager(app)
manager.add_command('runserver', Server(host='127.0.0.1', port=5000))

if __name__ == '__main__':
    app.config.from_object(config['development'])
    manager.run()
