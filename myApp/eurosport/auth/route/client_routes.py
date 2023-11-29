from flask import Blueprint, request, jsonify
from ..service.client_service import get_all_clients_service,get_client_by_id_service, add_client_service, update_client_service, delete_client_service

client_bp = Blueprint('client_bp', __name__)

# Adjust the route to be '/' since 'url_prefix' in Blueprint registration will handle the '/clients' part
@client_bp.route('/', methods=['GET'])
def get_clients():
    clients = get_all_clients_service()
    return jsonify([client.to_dict() for client in clients]), 200

@client_bp.route('/<int:entity_id>', methods=['GET'])
def get_client_by_id(entity_id):
    client = get_client_by_id_service(entity_id)
    if client is None:
        return jsonify({'message': 'Client not found'}), 404
    return jsonify(client.to_dict()), 200

# This route is okay since it's a POST request to the same base path '/clients'
@client_bp.route('/', methods=['POST'])  # Adjusted to '/'
def add_client():
    data = request.get_json()
    new_client = add_client_service(data)
    return jsonify(new_client.to_dict()), 201

@client_bp.route('/<int:entity_id>', methods=['PUT'])
def update_entity(entity_id):
    data = request.get_json()
    updated_entity = update_client_service(entity_id, data)
    if updated_entity is None:
        return jsonify({'message': 'Client not found'}), 404
    return jsonify(updated_entity.to_dict()), 200

@client_bp.route('/<int:entity_id>', methods=['DELETE'])
def delete_entity(entity_id):
    delete_client_service(entity_id)
    return '', 204