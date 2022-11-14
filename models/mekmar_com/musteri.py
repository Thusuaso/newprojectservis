from marshmallow import Schema,fields


class SiteMusteriSchema(Schema):
    id = fields.Int()
    adi = fields.String()
    kullaniciadi = fields.String()
    mailadres = fields.String()
    telefon = fields.String()


class SiteMusteriModel:

    id = None 
    adi = ""
    kullaniciadi = ""
    mailadres = ""
    telefon = ""