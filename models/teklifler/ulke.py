from marshmallow import Schema,fields


class UlkeSchema(Schema):
    id = fields.Int()
    ulkeAdi = fields.String()
    kod = fields.String()
    icon_Flags = fields.String()
    png_Flags = fields.String()


class UlkeModel:

    id = None
    ulkeAdi = ""
    kod = ""
    icon_Flags = ""
    png_Flags = ""

    