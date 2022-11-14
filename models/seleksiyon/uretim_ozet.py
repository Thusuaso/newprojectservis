from marshmallow import Schema,fields


class UretimOzetSchema(Schema):
    id = fields.Int()
    tanim = fields.String()
    gun = fields.Float()
    ay = fields.Float()
    yil = fields.Float()


class UretimOzetModel:
    id = None 
    tanim = ""
    gun = 0
    ay = 0
    yil = 0
    