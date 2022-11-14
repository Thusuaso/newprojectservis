from marshmallow import Schema,fields


class FirmaListeSchema(Schema):
    id = fields.Int() 
    firma_adi = fields.String()
   

class FirmaListeModel:

    id = None 
    firma_adi = ""