# coding=utf-8

from sqlalchemy import Column, String, Float, DateTime
from marshmallow import Schema, fields
from .entity import Entity, Base


# class Sensors(Entity, Base):
# #     __tablename__ = 'sensors'
# #
# #     sensor_id = Column(String)
# #     room = Column(String)
# #
# #
# #     def __init__(self, sensor_id, room, temp, humidity, measurement_time):
# #         Entity.__init__(self)
# #         self.sensor_id = sensor_id
# #         self.room = room
# #
# #
# # class HumidityMeasureSchema(Schema):
# #     uuid = fields.Str()
# #     id = fields.Str()
# #     room = fields.Str()
# #     created_at =fields.DateTime()
# #     updated_at = fields.DateTime()