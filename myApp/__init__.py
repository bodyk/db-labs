import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # Load and parse the YAML configuration file
    with open('myApp/config/app.yaml', 'r') as yaml_config:
        config = yaml.safe_load(yaml_config)
    app.config.update(config)

    db.init_app(app)

    # Import Blueprints and register them after initializing 'db' to avoid circular imports
    from myApp.eurosport.auth.route.client_routes import client_bp
    from myApp.eurosport.auth.route.trainer_routes import trainer_bp
    from myApp.eurosport.auth.route.equipment_routes import equipment_bp

    app.register_blueprint(client_bp, url_prefix='/clients')
    app.register_blueprint(trainer_bp, url_prefix='/trainers')
    app.register_blueprint(equipment_bp, url_prefix='/equipment')

    return app