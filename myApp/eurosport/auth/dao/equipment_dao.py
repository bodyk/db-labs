from myApp import db
from ..domain.models import Equipment

def get_all_equipment():
    return Equipment.query.all()

def get_equipment_by_id(equipment_id):
    return Equipment.query.get(equipment_id)

def add_equipment(equipment_data):
    new_equipment = Equipment(**equipment_data)
    db.session.add(new_equipment)
    db.session.commit()
    return new_equipment

def update_equipment(equipment_id, equipment_data):
    equipment = get_equipment_by_id(equipment_id)
    if equipment:
        for key, value in equipment_data.items():
            setattr(equipment, key, value)
        db.session.commit()
        return equipment
    return None

def delete_equipment(equipment_id):
    equipment = get_equipment_by_id(equipment_id)
    if equipment:
        db.session.delete(equipment)
        db.session.commit()
        return equipment
    return None
