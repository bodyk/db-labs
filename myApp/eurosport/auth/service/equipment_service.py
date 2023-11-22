from ..dao.equipment_dao import get_all_equipment, get_equipment_by_id, add_equipment, update_equipment, delete_equipment

def get_all_equipment_service():
    return get_all_equipment()

def get_equipment_by_id_service(equipment_id):
    return get_equipment_by_id(equipment_id)

def add_equipment_service(equipment_data):
    return add_equipment(equipment_data)

def update_equipment_service(equipment_id, equipment_data):
    return update_equipment(equipment_id, equipment_data)

def delete_equipment_service(equipment_id):
    return delete_equipment(equipment_id)
