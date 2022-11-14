from marshmallow import Schema,fields


class MusteriOdemeSchema(Schema):
    id = fields.Int()
    tarih = fields.String()
    tutar = fields.Float()


class MusteriOdemeModel:
    id = None 
    tarih = ""
    tutar = 0


