from marshmallow import Schema,fields


class YuzeySchema(Schema):
    id = fields.Int() 
    islemAdi = fields.String()
    sira = fields.Int() 


class YuzeyModel:
    id = None 
    islemAdi = fields.String()
    sira = fields.Int()