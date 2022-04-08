from flask import Blueprint, request
health_api = Blueprint('/', __name__)

@health_api.route('/health', methods=['GET'])
def health():
    return "pong", 200