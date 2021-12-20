# coding=utf-8

from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.orm import synonym
from marshmallow import Schema, fields
from .entity import Entity, Base
from datetime import datetime


class HumidityMeasure(Entity, Base):
    __tablename__ = 'humidity'

    sensor_id = Column(String)
    room = Column(String)
    temp = Column(Float)
    humidity = Column(Float)
    measurement_time = Column("timestamp", DateTime)

    def __init__(self, sensor_id, room, temp, humidity, measurement_time):
        Entity.__init__(self)
        self.sensor_id = sensor_id
        self.room = room
        self.temp = temp
        self.humidity = humidity
        self.measurement_time = measurement_time


class HumidityMeasureSchema(Schema):
    uuid = fields.Str()
    id = fields.Integer()
    sensor_id = fields.Str()
    room = fields.Str()
    temp = fields.Float()
    humidity = fields.Float()
    measurement_time = fields.DateTime()
    created_at =fields.DateTime()
    updated_at = fields.DateTime()