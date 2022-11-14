from marshmallow import Schema,fields


class FaturaListeSchema(Schema):
    id = fields.Int() 
    tur = fields.String()
   

class FaturaListeModel:

    id = None 
    tur = ""
    