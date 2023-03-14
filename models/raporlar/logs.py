from marshmallow import Schema,fields

class LogsMaliyetSchema(Schema):
    id = fields.Int()
    kayit_tarihi = fields.String()
    siparis_no = fields.String()
    yukleme_tarihi = fields.String()
    info = fields.String()
    kayit_kisi = fields.String()
    yil = fields.String()
    ay = fields.String()
    gun = fields.String()
    
class LogsMaliyetModel:
    id = 0
    kayit_tarihi = ""
    siparis_no = ""
    yukleme_tarihi = ""
    info = ""
    kayit_kisi = ""
    yil = ""
    ay = ""
    gun = ""