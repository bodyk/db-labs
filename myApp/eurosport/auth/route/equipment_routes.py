from flask import Blueprint, request, jsonify
from ..service.equipment_service import get_all_equipment_service, add_equipment_service

equipment_bp = Blueprint('equipment_bp', __name__)

@equipment_bp.route('/', methods=['GET'])
def get_equipment():
    equipment = get_all_equipment_service()
    return jsonify([eq.to_dict() for eq in equipment]), 200

@equipment_bp.route('/', methods=['POST'])
def add_equipment():
    data = request.get_json()
    new_equipment = add_equipment_service(data)
    return jsonify(new_equipment.to_dict()), 201
