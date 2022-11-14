from marshmallow import Schema,fields


class TemsilciOzetSchema(Schema):
    id = fields.Int()
    adi = fields.String()
    teklifSayisi = fields.Int()
    proformaSayisi = fields.Int()

class TemsilciOzetModel:
    id = None 
    adi = ""
    teklifSayisi = 0 
    proformaSayisi = 0