from marshmallow import Schema,fields


class EbatSchema(Schema):
    id = fields.String()
    ebat = fields.String()
    sira = fields.Int()
    #custom alanlar
    birim = fields.String()
    fiyat = fields.Float()
    getEbat = fields.String()


class EbatModel:

    id = ""
    ebat = ""
    sira = None
    birim = "",
    fiyat = 0
    getEbat = ""

    