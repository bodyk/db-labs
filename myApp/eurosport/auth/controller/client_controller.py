from flask import Blueprint, request, jsonify
from ..service.client_service import (
    get_all_clients_service, 
    add_client_service, 
    update_client_service, 
    delete_client_service
)

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = get_all_clients_service()
    return jsonify([client.to_dict() for client in clients]), 200

@client_bp.route('/clients', methods=['POST'])
def add_client():
    data = request.get_json()
    new_client = add_client_service(data)
    return jsonify(new_client.to_dict()), 201

@client_bp.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    data = request.get_json()
    updated_client = update_client_service(client_id, data)
    if updated_client:
        return jsonify(updated_client.to_dict()), 200
    else:
        return jsonify({"error": "Client not found"}), 404

@client_bp.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    deleted_client = delete_client_service(client_id)
    if deleted_client:
        return jsonify(deleted_client.to_dict()), 200
    else:
        return jsonify({"error": "Client not found"}), 404
