from ..dao.trainer_dao import get_all_trainers, get_trainer_by_id, add_trainer, update_trainer, delete_trainer

def get_all_trainers_service():
    return get_all_trainers()

def get_trainer_by_id_service(trainer_id):
    return get_trainer_by_id(trainer_id)

def add_trainer_service(trainer_data):
    return add_trainer(trainer_data)

def update_trainer_service(trainer_id, trainer_data):
    return update_trainer(trainer_id, trainer_data)

def delete_trainer_service(trainer_id):
    return delete_trainer(trainer_id)
