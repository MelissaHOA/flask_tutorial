import os

from flask import Flask


def create_app(test_config=None):
    # créer et configurer l'application
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # charger la configuration de l'instance, si elle existe, lorsque vous ne testez pas
        app.config.from_pyfile('config.py', silent=True)
    else:
        # charger la configuration de test si elle est transmise
        app.config.from_mapping(test_config)

    # assurez-vous que le dossier d'instance existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # une page simple qui dit bonjour
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app