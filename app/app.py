import os
from flask import Flask

from .config.config import config as cfg
from .controller.blacklist import blacklist
from .controller.health import health_api

def create_app(env='production'):
    app = Flask(__name__)
    app.config.from_object(cfg[env])
    app.register_blueprint(blacklist, url_prefix='/blacklists')
    app.register_blueprint(health_api, url_prefix='/blacklists')
    return app