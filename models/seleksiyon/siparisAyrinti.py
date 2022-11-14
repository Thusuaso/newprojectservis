from marshmallow import Schema,fields


class SiparisAyrintiSchema(Schema):
    id = fields.Int()
    urunkart_id = fields.Int()
    tanim = fields.String()
    siparisno = fields.String()
    urunbirimid = fields.Int()
    tedarikci = fields.String()
    
    

class SiparisAyrintiModel:
    id = None 
    urunkart_id = None 
    tanim = ""
    siparisno = ""
    urunbirimid = None 
    tedarikci = ""