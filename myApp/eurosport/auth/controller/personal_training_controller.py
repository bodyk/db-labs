from flask import Blueprint, request, jsonify
from ..service.personal_training_service import (
    get_all_service, 
    add_service, 
    update_service, 
    delete_service
)

personal_training_bp = Blueprint('personal_training_bp', __name__)

@personal_training_bp.route('/personal_trainings', methods=['GET'])
def get_personal_trainings():
    personal_trainings = get_all_service()
    return jsonify([personal_training.to_dict() for personal_training in personal_trainings]), 200

@personal_training_bp.route('/personal_trainings', methods=['POST'])
def add_personal_training():
    data = request.get_json()
    new_personal_training = add_service(data)
    return jsonify(new_personal_training.to_dict()), 201

@personal_training_bp.route('/personal_trainings/<int:personal_training_id>', methods=['PUT'])
def update_personal_training(personal_training_id):
    data = request.get_json()
    updated_personal_training = update_service(personal_training_id, data)
    if updated_personal_training:
        return jsonify(updated_personal_training.to_dict()), 200
    else:
        return jsonify({"error": "personal_training not found"}), 404

@personal_training_bp.route('/personal_trainings/<int:personal_training_id>', methods=['DELETE'])
def delete_personal_training(personal_training_id):
    deleted_personal_training = delete_service(personal_training_id)
    if deleted_personal_training:
        return jsonify(deleted_personal_training.to_dict()), 200
    else:
        return jsonify({"error": "personal_training not found"}), 404
