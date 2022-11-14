from marshmallow import Schema,fields


class OdemeListeSchema(Schema):

    id = fields.Int()
    tarih =  fields.String()
    musteriadi = fields.String()
    tutar = fields.Float()
    po = fields.String()
    status = fields.String()


class OdemeListeModel:
    id = None
    tarih = ""
    musteriadi = ""
    tutar = 0
    po = ""
    status = ""

