
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()

class BlackList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    app_uuid = db.Column(db.String(255))
    blocked_reason = db.Column(db.String(255), nullable=True)
    ip = db.Column(db.String(255))
    date_created = db.Column(db.String(255))

class BlackListSchema(SQLAlchemyAutoSchema):
    class Meta:
         model = BlackList
         include_relationships = True
         load_instance = True