from marshmallow import Schema,fields,validate


class AllOrdersSchema(Schema):
    id = fields.Int()
    siparisNo = fields.String()
    musteriId = fields.Int()
    musteri = fields.String()
    
class AllOrdersModel:
    
    id = 0
    siparisNo = ""
    musteriId = 0
    musteri = ""
    