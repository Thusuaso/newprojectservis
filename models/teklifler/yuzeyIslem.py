from marshmallow import Schema,fields


class YuzeyIslemSchema(Schema):
    id = fields.Int()
    islemAdi = fields.String()
    sira = fields.Int()


class YuzeyIslemModel:

    id = None
    islemAdi = ""
    sira = None

   