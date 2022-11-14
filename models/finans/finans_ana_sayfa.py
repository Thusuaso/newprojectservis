from marshmallow import Schema,fields


class FinansAnaSayfaSchema(Schema):

    id = fields.Int()
    musteriadi = fields.String()
    devir = fields.Float()
    ciro = fields.Float()
    odenen = fields.Float()
    bakiye = fields.Float()
    pesinat = fields.Float()
    genel_bakiye = fields.Float()
    eski_pesinat = fields.Float()
    temsilci = fields.String()
    marketing = fields.String()
    operasyon = fields.String()
    finansman = fields.String()
    yeni_borc = fields.Float()
    eski_borc = fields.Float()
    po = fields.String()
    ulke = fields.String()
    kapanmayan_siparis = fields.Float()
    kapanmayan_kalan = fields.Float()
    kapanmayan_odenen = fields.Float()


class FinansAnaSayfaModel:

    id = None 
    musteriadi = ""
    devir = 0 
    ciro = 0 
    odenen = 0 
    bakiye = 0
    pesinat = 0
    genel_bakiye = 0
    eski_pesinat = 0
    temsilci = ""
    marketing = ""
    operasyon = ""
    finansman = ""
    yeni_borc = 0
    eski_borc = 0
    po = ""
    ulke = ""
    kapanmayan_siparis = 0
    kapanmayan_kalan = 0
    kapanmayan_odenen = 0