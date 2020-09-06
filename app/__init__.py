from flask import Flask

from .site.routes import site
from .config.routes import config

def create_app():
    app = Flask(__name__)
    app.register_blueprint(site)
    app.register_blueprint(config)
    return app
