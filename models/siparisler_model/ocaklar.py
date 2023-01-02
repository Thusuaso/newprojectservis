from marshmallow import Schema,fields

class OcakListSchema(Schema):
    id = fields.Int()
    mineName = fields.String()
    
class OcakListModel:
    id = 0
    mineName = ""