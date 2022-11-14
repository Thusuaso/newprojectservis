from marshmallow import Schema,fields


class EfesFinansAnaSayfaSchema(Schema):

    id = fields.Int()
    musteriadi = fields.String()
    devir = fields.Float()
    ciro = fields.Float()
    odenen = fields.Float()
    bakiye = fields.Float()
    pesinat = fields.Float()
    genel_bakiye = fields.Float()
    eski_pesinat = fields.Float()
    kapanmayan_siparis = fields.Float()
    kapanmayan_kalan = fields.Float()
    kapanmayan_odenen = fields.Float()


class EfesFinansAnaSayfaModel:

    id = None 
    musteriadi = ""
    devir = 0 
    ciro = 0 
    odenen = 0 
    bakiye = 0
    pesinat = 0
    genel_bakiye = 0
    eski_pesinat = 0
    kapanmayan_siparis = 0
    kapanmayan_kalan = 0
    kapanmayan_odenen = 0

class EfesFinansGelenOdemelerSchema(Schema):
    yil=fields.Int()
    gelen_odeme=fields.Float()
    
class EfesFinansGelenOdemelerModel:
    yil = 0
    gelen_odeme=0