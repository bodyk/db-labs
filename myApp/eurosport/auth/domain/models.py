from flask_sqlalchemy import SQLAlchemy
from myApp import db

class Time(db.Model):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(15), nullable=True)
    time_start = db.Column(db.String(45), nullable=False)
    time_end = db.Column(db.String(45), nullable=False)
    services = db.relationship('Service', backref='time', lazy=True)
    group_trainings = db.relationship('GroupTraining', backref='time', lazy=True)

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    trainer_services = db.relationship('TrainerService', backref='service', lazy='dynamic')

class Trainer(db.Model):
    __tablename__ = 'trainer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(12), nullable=True)
    group_trainings = db.relationship('GroupTraining', backref='trainer', lazy=True)
    trainer_services = db.relationship('TrainerService', backref='trainer', lazy='dynamic')

class MembershipCardType(db.Model):
    __tablename__ = 'membership_card_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    clients = db.relationship('Client', backref='membership_card_type', lazy=True)

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    surname = db.Column(db.String(45), nullable=False)
    phone = db.Column(db.String(12), nullable=True)
    membership_card_type_id = db.Column(db.Integer, db.ForeignKey('membership_card_type.id'), nullable=False)
    client_trainings = db.relationship('ClientTraining', backref='client', lazy=True)

class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    area = db.Column(db.Float, nullable=True)
    equipments = db.relationship('Equipment', backref='room', lazy=True)

class Equipment(db.Model):
    __tablename__ = 'equipment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=True)
    serial_number = db.Column(db.String(45), nullable=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    personal_training_equipment = db.relationship('PersonalTrainingEquipment', backref='equipment', lazy='dynamic')

class GroupTraining(db.Model):
    __tablename__ = 'group_training'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=False)
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'), nullable=False)
    client_trainings = db.relationship('ClientTraining', backref='group_training', lazy=True)

class TrainerService(db.Model):
    __tablename__ = 'trainer_service'
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)

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
    personal_training_equipment = db.relationship('PersonalTrainingEquipment', backref='personal_training', lazy='dynamic')

class PersonalTrainingEquipment(db.Model):
    __tablename__ = 'personal_training_equipment'
    personal_training_id = db.Column(db.Integer, db.ForeignKey('personal_training.id'), primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), primary_key=True)
