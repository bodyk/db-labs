from flask import Blueprint, request, jsonify
from ..service.equipment_service import (
    get_all_equipment_service, 
    add_equipment_service, 
    update_equipment_service, 
    delete_equipment_service
)

equipment_bp = Blueprint('equipment_bp', __name__)

@equipment_bp.route('/equipment', methods=['GET'])
def get_equipment():
    equipment_list = get_all_equipment_service()
    return jsonify([equipment.to_dict() for equipment in equipment_list]), 200

@equipment_bp.route('/equipment', methods=['POST'])
def add_equipment():
    data = request.get_json()
    new_equipment = add_equipment_service(data)
    return jsonify(new_equipment.to_dict()), 201

@equipment_bp.route('/equipment/<int:equipment_id>', methods=['PUT'])
def update_equipment(equipment_id):
    data = request.get_json()
    updated_equipment = update_equipment_service(equipment_id, data)
    if updated_equipment:
        return jsonify(updated_equipment.to_dict()), 200
    else:
        return jsonify({"error": "Equipment not found"}), 404

@equipment_bp.route('/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_equipment(equipment_id):
    deleted_equipment = delete_equipment_service(equipment_id)
    if deleted_equipment:
        return jsonify(deleted_equipment.to_dict()), 200
    else:
        return jsonify({"error": "Equipment not found"}), 404
