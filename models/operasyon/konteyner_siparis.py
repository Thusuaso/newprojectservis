from marshmallow import Schema,fields


class SiparisListeSchema(Schema):
    id = fields.Int() 
    siparis_no = fields.String()
   

class SiparisListeModel:

    id = None 
    siparis_no = ""