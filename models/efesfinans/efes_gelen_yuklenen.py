from marshmallow import Schema,fields

class EfesGelenYuklenenSchema(Schema):
    tumSatislar = fields.Float()
    tumSatislarFob = fields.Float()
    yuklenmemisSatislar = fields.Float()
    yuklenmisSatislar = fields.Float()
    yil = fields.String()
    tahminiTumSatislar = fields.Float()
    
class EfesGelenYuklenenModel:
    tumSatislarFob=0
    tumSatislar = 0
    yuklenmemisSatislar = 0
    yuklenmisSatislar = 0
    yil=0
    tahminiTumSatislar = 0