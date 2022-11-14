from marshmallow import Schema,fields


class YuzeyKenarSchema(Schema):
    id = fields.Int()
    yuzeyIslemAdi = fields.String()
    kullaniciId = fields.Int()

    #custom alanlar 
    yuzey_1 = fields.String()
    yuzey_2 = fields.String()
    yuzey_3 = fields.String()


class YuzeyKenarModel:

    id = None
    yuzeyIslemAdi = ""
    kullaniciId = None

    #custom alanlar
    yuzey_1 = ""
    yuzey_2 = ""
    yuzey_3 = ""
   