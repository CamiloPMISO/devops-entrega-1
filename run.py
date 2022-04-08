import os

from flask_jwt_extended import JWTManager

from app.app import create_app
from app.models.model import db

if __name__ == '__main__':
    env = os.getenv('ENV', 'development')
    app = create_app(env)
    app_context = app.app_context()
    app_context.push()
    db.init_app(app)
    db.create_all()
    jwt = JWTManager(app)
    app.run(host='0.0.0.0', port=5001)
