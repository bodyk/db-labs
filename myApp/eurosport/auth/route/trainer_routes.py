from flask import Blueprint, request, jsonify
from ..service.trainer_service import get_all_trainers_service, add_trainer_service

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
