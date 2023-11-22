from flask import Blueprint, request, jsonify
from ..service.trainer_service import get_all_trainers_service, add_trainer_service, update_trainer_service, delete_trainer_service

trainer_bp = Blueprint('trainer_bp', __name__)

@trainer_bp.route('/', methods=['GET'])
def get_trainers():
    trainers = get_all_trainers_service()
    return jsonify([trainer.to_dict() for trainer in trainers]), 200

@trainer_bp.route('/', methods=['POST'])
def add_trainer():
    data = request.get_json()
    new_trainer = add_trainer_service(data)
    return jsonify(new_trainer.to_dict()), 201

@trainer_bp.route('/<int:entity_id>', methods=['PUT'])
def update_entity(entity_id):
    data = request.get_json()
    updated_entity = update_trainer_service(entity_id, data)
    return jsonify(updated_entity.to_dict()), 200

@trainer_bp.route('/<int:entity_id>', methods=['DELETE'])
def delete_entity(entity_id):
    delete_trainer_service(entity_id)
    return '', 204