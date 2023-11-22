from flask import Blueprint, request, jsonify
from ..service.trainer_service import (
    get_all_trainers_service, 
    add_trainer_service, 
    update_trainer_service, 
    delete_trainer_service
)

trainer_bp = Blueprint('trainer_bp', __name__)

@trainer_bp.route('/trainers', methods=['GET'])
def get_trainers():
    trainers = get_all_trainers_service()
    return jsonify([trainer.to_dict() for trainer in trainers]), 200

@trainer_bp.route('/trainers', methods=['POST'])
def add_trainer():
    data = request.get_json()
    new_trainer = add_trainer_service(data)
    return jsonify(new_trainer.to_dict()), 201

@trainer_bp.route('/trainers/<int:trainer_id>', methods=['PUT'])
def update_trainer(trainer_id):
    data = request.get_json()
    updated_trainer = update_trainer_service(trainer_id, data)
    if updated_trainer:
        return jsonify(updated_trainer.to_dict()), 200
    else:
        return jsonify({"error": "Trainer not found"}), 404

@trainer_bp.route('/trainers/<int:trainer_id>', methods=['DELETE'])
def delete_trainer(trainer_id):
    deleted_trainer = delete_trainer_service(trainer_id)
    if deleted_trainer:
        return jsonify(deleted_trainer.to_dict()), 200
    else:
        return jsonify({"error": "Trainer not found"}), 404
