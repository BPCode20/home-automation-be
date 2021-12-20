# coding=utf-8
from marshmallow import Schema, fields
from flask import jsonify
from datetime import datetime

def baseError(httpStatusCode, errorCode ,errorMessage):
    escapedStatusCode = int(httpStatusCode)
    error = {'code': errorCode, 'messages': errorMessage}
    server = {'time': datetime.now()}
    errorResponse = {'httpStatusCode': escapedStatusCode, 'server': server, 'error': error}
    return jsonify(ErrorResponseSchema().dump(errorResponse)), escapedStatusCode

def badRequest(errorMessage, errorCode = "BAD_REQUEST"):
    return baseError(400, errorCode, errorMessage)

def notFound(errorMessage, errorCode = "NOT_FOUND"):
    return baseError(404, errorCode, errorMessage)

class ServerSchema(Schema):
    time = fields.DateTime()

class ErrorSchema(Schema):
    code = fields.Str()
    messages = fields.Str()

class ErrorFields(Schema):
    fieldValue = fields.Str()

class ErrorResponseSchema(Schema):
    httpStatusCode = fields.Integer()
    server = fields.Nested(ServerSchema)
    error = fields.Nested(ErrorSchema)
#    errorFields = fields.Nested(ErrorFields)
