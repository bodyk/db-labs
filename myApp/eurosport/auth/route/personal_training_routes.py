from flask import Blueprint, request, jsonify
from ..service.personal_training_service import get_all, add_service, update_service, delete_service

personal_training_bp = Blueprint('personal_training_bp', __name__)

# Adjust the route to be '/' since 'url_prefix' in Blueprint registration will handle the '/personal_trainings' part
@personal_training_bp.route('/', methods=['GET'])
def get_personal_trainings():
    personal_trainings = get_all()
    return jsonify([personal_training.to_dict() for personal_training in personal_trainings]), 200

# This route is okay since it's a POST request to the same base path '/personal_trainings'
@personal_training_bp.route('/', methods=['POST'])  # Adjusted to '/'
def add_personal_training():
    data = request.get_json()
    new_personal_training = add_service(data)
    return jsonify(new_personal_training.to_dict()), 201

@personal_training_bp.route('/<int:entity_id>', methods=['PUT'])
def update_entity(entity_id):
    data = request.get_json()
    updated_entity = update_service(entity_id, data)
    return jsonify(updated_entity.to_dict()), 200

@personal_training_bp.route('/<int:entity_id>', methods=['DELETE'])
def delete_entity(entity_id):
    delete_service(entity_id)
    return '', 204