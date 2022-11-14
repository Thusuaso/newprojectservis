from marshmallow import Schema,fields


class EnBoySchema(Schema):
    id = fields.Int() 
    enBoy = fields.String()
    sira = fields.Int() 

class EnBoyModel:
    id = None 
    enBoy = ""
    sira = 0