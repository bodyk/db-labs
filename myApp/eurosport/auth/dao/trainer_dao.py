from myApp import db
from ..domain.models import Trainer

def get_all_trainers():
    return Trainer.query.all()

def get_trainer_by_id(trainer_id):
    return Trainer.query.get(trainer_id)

def add_trainer(trainer_data):
    new_trainer = Trainer(**trainer_data)
    db.session.add(new_trainer)
    db.session.commit()
    return new_trainer

def update_trainer(trainer_id, trainer_data):
    trainer = get_trainer_by_id(trainer_id)
    if trainer:
        for key, value in trainer_data.items():
            setattr(trainer, key, value)
        db.session.commit()
        return trainer
    return None

def delete_trainer(trainer_id):
    trainer = get_trainer_by_id(trainer_id)
    if trainer:
        db.session.delete(trainer)
        db.session.commit()
        return trainer
    return None
