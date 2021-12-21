from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        from .src.sensor_api import sensor_blueprint
        app.register_blueprint(sensor_blueprint)

    return app
