from marshmallow import Schema,fields



class OdemeAySchema(Schema):

    id = fields.Int()
    ay = fields.Int()
    ay_str = fields.String()

class OdemeAyModel:

    id = None
    ay = 0
    ay_str = ""