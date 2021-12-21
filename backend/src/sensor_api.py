# coding=utf-8

from flask import Blueprint, jsonify, request
from flask_cors import CORS
from .entities.entity import Session, engine, Base
from .entities.temp_humidity import HumidityMeasure, HumidityMeasureSchema
from .errorResponse import *
import string
import re


# Blueprint
sensor_blueprint = Blueprint('sensor_blueprint', __name__)
# if needed, generate database schema
Base.metadata.create_all(engine)


@sensor_blueprint.route('/temp-humidity')
def get_all_measurements():
    # fetching from the database
    pattern = re.compile("[A-Z0-9_]{0,20}")
    session = Session()
    filter_options = {}
    if request.args.get('sensorId'):
        try:
            filter_options["sensor_id"] = str(int(request.args.get('sensorId')))
        except ValueError:
            return badRequest("This is not a valid input. Id must be Integer.")
    if request.args.get('room'):
        try:
            room_str = str(request.args.get('room'))
            if not pattern.match(room_str):
                raise ValueError
            filter_options["room"] = room_str
        except ValueError:
            return badRequest("This is not a valid input. Id must be Integer.")
    if filter_options:
        exam_objects = session.query(HumidityMeasure).filter_by(**filter_options)
    else:
        exam_objects = session.query(HumidityMeasure).all()

    # transforming into JSON-serializable objects
    schema = HumidityMeasureSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(exams)

@sensor_blueprint.route('/temp-humidity/<id>')
def get_measurement_by_id(id):
    # fetching from the database
    measuementId = None
    try:
        measuementId = int(id)
    except ValueError:
        return badRequest( "This is not a valid input. Id must be Integer.")
    session = Session()
    exam_objects = session.query(HumidityMeasure).get(measuementId)

    # transforming into JSON-serializable objects
    schema = HumidityMeasureSchema(many=True)
    exams = schema.dump(exam_objects)

    # serializing as JSON
    session.close()
    return jsonify(exams)

@sensor_blueprint.route('/temp-humidity', methods=['POST'])
def add_humidity_measurement():
    # mount exam object
    print(request.get_json())
    data = request.get_json()
    if "measurement_time" in data:
        # print(data["measurement_time"])
        data["measurement_time"] = datetime.utcfromtimestamp(data["measurement_time"]).strftime('%Y-%m-%d %H:%M:%S')
        # print(data["measurement_time"])
        # print(type(data["measurement_time"]))
    posted_measurement = HumidityMeasureSchema(only=('sensor_id','room', 'temp', 'humidity', 'measurement_time')) \
        .load(request.get_json())

    measurement = HumidityMeasure(**posted_measurement)

    # persist exam
    session = Session()
    session.add(measurement)
    session.commit()

    # return created exam
    new_measurement = HumidityMeasureSchema().dump(measurement)
    session.close()
    print(new_measurement)
    return jsonify(new_measurement), 201


@sensor_blueprint.route('/bulk/temp-humidity', methods=['POST'])
def add_bulk_humidity_measurement():
    # mount exam object
    posted_measurement = HumidityMeasureSchema(many=True, only=('sensor_id','room', 'temp', 'humidity', 'measurement_time')) \
        .load(request.get_json())

    measurements = [HumidityMeasure(**measuremnt) for measuremnt in posted_measurement]

    # persist exam
    session = Session()
    session.bulk_save_objects(measurements)
    session.commit()

    # return created exaßm
    new_measurements = HumidityMeasureSchema(many=True).dump(measurements)
    session.close()
    return jsonify(new_measurements), 201


@sensor_blueprint.route('/sensors')
def get_sensors():
    # fetching from the database
    session = Session()

    assurances = []
    for assurance in session.query(HumidityMeasure.sensor_id).distinct():
        assurances.append(assurance.sensor_id)
    # transforming into JSON-serializable objects
    # schema = HumidityMeasureSchema(many=True)
    # exams = schema.dump(assurances)

    # serializing as JSON
    session.close()
    return jsonify(assurances)

@sensor_blueprint.route('/rooms')
def get_rooms():
    if request.args.get('includeSensors'):
        try:
            include_sensors = bool(request.args.get('includeSensors'))
        except ValueError:
            return badRequest("This is not a valid input. IncludeSensors must be Bool.")
    session = Session()
    rooms = []
    for result in session.query(HumidityMeasure.room).distinct():
        rooms.append(result.room)
    # serializing as JSON
    # if include_sensors:
    #     for i, room in enumerate(rooms):
    #         sensor_id = session.query(HumidityMeasure.room).filter_by(room=room).order_by(HumidityMeasure.measurement_time.desc())
    #         rooms[i]["sensorId"] = sensor_id
    session.close()
    return jsonify(rooms)
