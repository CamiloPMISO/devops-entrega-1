from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from ..services.blacklist import BlackListService

blacklist = Blueprint('blacklist_api', __name__)

@blacklist.route('', methods=['POST'])
@jwt_required()
def add():
    req = request.json

    blacklist_service = BlackListService()

    req['ip'] = request.remote_addr

    resp = blacklist_service.add(req)

    return resp, 200


@blacklist.route('/', methods=['GET'])
def get():
    # Agregar logica get Manuel
    return "", 200