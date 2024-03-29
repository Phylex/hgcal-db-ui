__version__ = "0.0.1"

import os
from flask import Flask


def create_app(test_config=None):
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'staging-db.sqlite'),
    )
    # Apply configuration to the app
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    db.init_app(app)
    from . import auth
    app.register_blueprint(auth.bp)

    return app
