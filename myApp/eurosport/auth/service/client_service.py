from ..dao.client_dao import get_all_clients, get_client_by_id, add_client, update_client, delete_client

def get_all_clients_service():
    return get_all_clients()

def get_client_by_id_service(client_id):
    return get_client_by_id(client_id)

def add_client_service(client_data):
    return add_client(client_data)

def update_client_service(client_id, client_data):
    return update_client(client_id, client_data)

def delete_client_service(client_id):
    return delete_client(client_id)
