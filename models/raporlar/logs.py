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
    yuklenen_bu_ay_sip = fields.Float()
    yuklenen_yil_sonu_tahmin = fields.Float()
    siparis_bu_ay = fields.Float()
    siparis_yil_sonu_tahmin = fields.Float()
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
    yuklenen_bu_ay_sip = 0
    yuklenen_yil_sonu_tahmin = 0
    siparis_bu_ay = 0
    siparis_yil_sonu_tahmin = 0