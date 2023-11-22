from flask import Blueprint, request, jsonify
from ..service.client_service import get_all_clients_service, add_client_service

client_bp = Blueprint('client_bp', __name__)

# Adjust the route to be '/' since 'url_prefix' in Blueprint registration will handle the '/clients' part
@client_bp.route('/', methods=['GET'])
def get_clients():
    clients = get_all_clients_service()
    return jsonify([client.to_dict() for client in clients]), 200

# This route is okay since it's a POST request to the same base path '/clients'
@client_bp.route('/', methods=['POST'])  # Adjusted to '/'
def add_client():
    data = request.get_json()
    new_client = add_client_service(data)
    return jsonify(new_client.to_dict()), 201