from marshmallow import Schema,fields


class TedarikciListeSchema(Schema):
    id = fields.Int()
    tedarikciadi = fields.String()
    siparis_sayisi = fields.Int()

class TedarikciListeModel:
    id = None
    tedarikciadi = ""
    siparis_sayisi = 0