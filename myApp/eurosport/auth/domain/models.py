from flask_sqlalchemy import SQLAlchemy
from myApp import db

class Time(db.Model):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(15), nullable=True)
    time_start = db.Column(db.String(45), nullable=False)
    time_end = db.Column(db.String(45), nullable=False)
    services = db.relationship('Service', back_populates='time', lazy=True)
    group_trainings = db.relationship('GroupTraining', primaryjoin="Time.id == GroupTraining.time_id", back_populates='time', lazy=True)

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
    trainer_services = db.relationship('TrainerService', back_populates='service', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'time_id': self.time_id
        }

class Trainer(db.Model):
    __tablename__ = 'trainer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(12), nullable=True)
    group_trainings = db.relationship('GroupTraining', primaryjoin="Trainer.id == GroupTraining.trainer_id", back_populates='trainer', lazy=True)
    trainer_services = db.relationship('TrainerService', back_populates='trainer', lazy=True)
    personal_trainings = db.relationship('PersonalTraining', back_populates='trainer', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone
        }

class MembershipCardType(db.Model):
    __tablename__ = 'membership_card_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    clients = db.relationship('Client', back_populates='membership_card_type', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
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
    personal_trainings = db.relationship('PersonalTraining', back_populates='client', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone,
            'membership_card_type_id': self.membership_card_type_id,
            'membership_card_type_name': self.membership_card_type.name,
            'personal_training_ids': [pt.id for pt in self.personal_trainings]
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
    room = db.relationship('Room', back_populates='equipments')
    personal_training_equipment = db.relationship('PersonalTrainingEquipment', back_populates='equipment', lazy='dynamic')
    personal_trainings = db.relationship('PersonalTraining', secondary='personal_training_equipment', back_populates='equipments')

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
    time = db.relationship('Time', back_populates='group_trainings')
    trainer = db.relationship('Trainer', back_populates='group_trainings')
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
            'service_id': self.service_id
        }

class ClientTraining(db.Model):
    __tablename__ = 'client_training'
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), primary_key=True)
    group_training_id = db.Column(db.Integer, db.ForeignKey('group_training.id'), primary_key=True)
    client = db.relationship('Client', back_populates='client_trainings')
    group_training = db.relationship('GroupTraining', back_populates='client_trainings')

    def to_dict(self):
        return {
            'client_id': self.client_id,
            'group_training_id': self.group_training_id
        }

class PersonalTraining(db.Model):
    __tablename__ = 'personal_training'
    id = db.Column(db.Integer, primary_key=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=False)
    trainer = db.relationship('Trainer', back_populates='personal_trainings')
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    client = db.relationship('Client', back_populates='personal_trainings')
    name = db.Column(db.String(45), nullable=True)
    personal_training_equipment = db.relationship('PersonalTrainingEquipment', back_populates='personal_training', lazy='dynamic')
    equipments = db.relationship('Equipment', secondary='personal_training_equipment', back_populates='personal_trainings')

    def to_dict(self):
        return {
            'id': self.id,
            'trainer_id': self.trainer_id,
            'client_id': self.client_id,
            'name': self.name,
            'client_details': {'id': self.client.id, 'name': self.client.name} if self.client else None,
            'trainer_details': {'id': self.trainer.id, 'name': self.trainer.name} if self.trainer else None,
            'equipment_ids': [equipment.id for equipment in self.equipments]
        }

class PersonalTrainingEquipment(db.Model):
    __tablename__ = 'personal_training_equipment'
    personal_training_id = db.Column(db.Integer, db.ForeignKey('personal_training.id'), primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), primary_key=True)
    
    # Relationship to the PersonalTraining model
    personal_training = db.relationship('PersonalTraining', back_populates='personal_training_equipment')

    # Relationship to the Equipment model
    equipment = db.relationship('Equipment', back_populates='personal_training_equipment')

    def to_dict(self):
        return {
            'personal_training_id': self.personal_training_id,
            'equipment_id': self.equipment_id
        }
