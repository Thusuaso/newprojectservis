from marshmallow import Schema,fields


class SiparisListeSchema(Schema):
    id = fields.Int() 
    siparisno = fields.String()
    musteriid = fields.Int()
    link = fields.String()

class SiparisListeModel:

    id = None 
    siparisno = ""
    musteriid = None 
    link =""
