from myApp import db
from ..domain.models import Client

def get_all_clients():
    return Client.query.all()

def get_client_by_id(client_id):
    return Client.query.get(client_id)

def add_client(client_data):
    new_client = Client(**client_data)
    db.session.add(new_client)
    db.session.commit()
    return new_client

def update_client(client_id, client_data):
    client = get_client_by_id(client_id)
    if client:
        for key, value in client_data.items():
            setattr(client, key, value)
        db.session.commit()
        return client
    return None

def delete_client(client_id):
    client = get_client_by_id(client_id)
    if client:
        db.session.delete(client)
        db.session.commit()
        return client
    return None
