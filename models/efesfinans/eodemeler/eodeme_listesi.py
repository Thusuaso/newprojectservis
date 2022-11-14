from marshmallow import Schema,fields


class EfesOdemeListeSchema(Schema):

    id = fields.Int()
    tarih =  fields.String()
    musteriadi = fields.String()
    siparisno = fields.String()
    tutar = fields.Float()


class EfesOdemeListeModel:
    id = None
    tarih = ""
    musteriadi = ""
    siparisno = ""
    tutar = 0

