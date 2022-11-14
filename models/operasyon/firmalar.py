from marshmallow import Schema,fields


class FirmaListeSchema(Schema):
    id = fields.Int() 
    firma_adi = fields.String()
    mail = fields.String()
    telefon = fields.String()
    aciklama = fields.String()

   

class FirmaListeModel:

    id = None 
    firma_adi = ""
    mail = ""
    telefon = ""
    aciklama = ""


class FirmaSchema(Schema):
    id = fields.Int() 
    firma_adi = fields.String()
    mail = fields.String()
    telefon = fields.String()
    aciklama = fields.String()

   

class FirmaModel:

    id = 0 
    firma_adi = ""
    mail = ""
    telefon = ""
    aciklama = ""    