from myApp import db
from ..domain.models import PersonalTraining

def get_all():
    return PersonalTraining.query.all()

def get_by_id(id):
    return PersonalTraining.query.get(id)

def add(data):
    new_data = PersonalTraining(**data)
    db.session.add(new_data)
    db.session.commit()
    return new_data

def update(id, data):
    entity = get_by_id(id)
    if entity:
        for key, value in data.items():
            setattr(entity, key, value)
        db.session.commit()
        return entity
    return None

def delete(id):
    entity = get_by_id(id)
    if entity:
        db.session.delete(entity)
        db.session.commit()
        return entity
    return None
