from marshmallow import Schema,fields



class EfesOdemeAySchema(Schema):

    id = fields.Int()
    ay = fields.Int()
    ay_str = fields.String()

class EfesOdemeAyModel:

    id = None
    ay = 0
    ay_str = ""