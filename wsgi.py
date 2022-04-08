import os

from flask_jwt_extended import JWTManager

from app.app import create_app
from app.models.model import db

env = os.getenv('ENV','production') 
app = create_app(env)
jwt = JWTManager(app)
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()