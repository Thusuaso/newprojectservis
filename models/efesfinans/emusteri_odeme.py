from marshmallow import Schema,fields


class EfesMusteriOdemeSchema(Schema):
    id = fields.Int()
    tarih = fields.String()
    tutar = fields.Float()


class EfesMusteriOdemeModel:
    id = None 
    tarih = ""
    tutar = 0


