from marshmallow import Schema,fields


class StyleSchema(Schema):
    backgroundColor = fields.String()

class StyleModel:
    backgroundColor = 'yellow'