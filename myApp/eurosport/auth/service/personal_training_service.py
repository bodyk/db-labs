from ..dao.personal_training_dao import get_all, get_by_id, add, update, delete

def get_all_service():
    return get_all()

def get_by_id_service(client_id):
    return get_by_id(client_id)

def add_service(client_data):
    return add(client_data)

def update_service(client_id, client_data):
    return update(client_id, client_data)

def delete_service(client_id):
    return delete(client_id)
