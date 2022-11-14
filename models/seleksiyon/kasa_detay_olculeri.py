from marshmallow import Schema,fields

class KasaDetayOlculeriSchema(Schema):
    id = fields.Int()
    ebat = fields.String()
    adet = fields.String()
    kasaOlculeri = fields.String()
    firmaadi = fields.String()

    


class KasaDetayModel:
    id=0
    ebat = ""
    adet = ""
    kasaOlculeri = ""
    firmaadi = ""
    
class TedarikcilerListSchema(Schema):
    id = fields.Int()
    firmaAdi = fields.String()
    
class TedarikcilerListModel:
    id = 0
    firmaAdi = ""
    


     

