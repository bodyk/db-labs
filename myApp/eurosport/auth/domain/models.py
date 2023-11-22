from flask_sqlalchemy import SQLAlchemy
from myApp import db

class Time(db.Model):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(15), nullable=True)
    time_start = db.Column(db.String(45), nullable=False)
    time_end = db.Column(db.String(45), nullable=False)
    services = db.relationship('Service', back_populates='time', lazy=True)
    group_trainings = db.relationship('GroupTraining', back_populates='time', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'day': self.day,
            'time_start': self.time_start,
            'time_end': self.time_end
        }

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    time = db.relationship('Time', back_populates='services')
    trainer_services = db.relationship('TrainerService', back_populates='service', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'time': self.time.to_dict() if self.time else None
        }

class Trainer(db.Model):
    __tablename__ = 'trainer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(12), nullable=True)
    group_trainings = db.relationship('GroupTraining', back_populates='trainer', lazy=True)
    trainer_services = db.relationship('TrainerService', back_populates='trainer', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone,
            'group_trainings': [training.to_dict() for training in self.group_trainings]
        }

class MembershipCardType(db.Model):
    __tablename__ = 'membership_card_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    clients = db.relationship('Client', back_populates='membership_card_type', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'clients': [client.to_dict() for client in self.clients]
        }

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(12), nullable=True)
    membership_card_type_id = db.Column(db.Integer, db.ForeignKey('membership_card_type.id'), nullable=False)
    membership_card_type = db.relationship('MembershipCardType', back_populates='clients')
    client_trainings = db.relationship('ClientTraining', back_populates='client', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone,
            'membership_card_type': self.membership_card_type.to_dict() if self.membership_card_type else None,
            'trainings': [training.to_dict() for training in self.client_trainings]
        }

class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    area = db.Column(db.Float, nullable=True)
    equipments = db.relationship('Equipment', back_populates='room', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'area': self.area
        }

class Equipment(db.Model):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=True)
    serial_number = db.Column(db.String(45), nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    personal_training_equipment = db.relationship('PersonalTrainingEquipment', back_populates='equipment', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'serial_number': self.serial_number,
            'room_id': self.room_id
        }

class GroupTraining(db.Model):
    __tablename__ = 'group_training'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=False)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    client_trainings = db.relationship('ClientTraining', back_populates='group_training', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'trainer_id': self.trainer_id,
            'time_id': self.time_id
        }

class TrainerService(db.Model):
    __tablename__ = 'trainer_service'
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    trainer = db.relationship('Trainer', back_populates='trainer_services')
    service = db.relationship('Service', back_populates='trainer_services')

    def to_dict(self):
        return {
            'trainer_id': self.trainer_id,
            'service_id': self.service_id,
            'trainer': self.trainer.to_dict() if self.trainer else None,
            'service': self.service.to_dict() if self.service else None
        }

class ClientTraining(db.Model):
    __tablename__ = 'client_training'
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), primary_key=True)
    group_training_id = db.Column(db.Integer, db.ForeignKey('group_training.id'), primary_key=True)

class PersonalTraining(db.Model):
    __tablename__ = 'personal_training'
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    name = db.Column(db.String(45), nullable=True)
    personal_training_equipment = db.relationship('PersonalTrainingEquipment', back_populates='personal_training', lazy='dynamic')

class PersonalTrainingEquipment(db.Model):
    __tablename__ = 'personal_training_equipment'
    personal_training_id = db.Column(db.Integer, db.ForeignKey('personal_training.id'), primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), primary_key=True)
