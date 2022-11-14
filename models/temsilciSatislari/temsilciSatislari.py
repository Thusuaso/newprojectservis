from marshmallow import Schema,fields


class TemsilciSatislariSchema(Schema):
    siparisTarihi = fields.String()
    siparisNo = fields.String()
    siparisTotal = fields.Float()
    yuklemeTarihi = fields.String()
    gelenOdemeler = fields.Float()
    yuklenmemisGelenBedel =fields.Float()
    yuklenmisGelenBedel = fields.Float()
    gelenBedelTarihi = fields.String()
    odenecekKalanBedel = fields.Float()
    aylikUretimdekiSiparisBedel = fields.Float()
    aylikUretimdekiSiparisMiktar = fields.Float()
    aylikSiparisTamamiBedel = fields.Float()
    aylikSiparisTamamiMiktar = fields.Float()
    ay = fields.String()
    background = fields.String()
    backgroundSatisSahibi = fields.String()

class TemsilciSatislariModel:

    siparisTarihi = ""
    siparisNo = ""
    siparisTotal = 0
    yuklemeTarihi=""
    gelenOdemeler = 0
    yuklenmemisGelenBedel = 0
    yuklenmisGelenBedel = 0
    gelenBedelTarihi = ""
    odenecekKalanBedel = 0
    aylikUretimdekiSiparisBedel = 0
    aylikUretimdekiSiparisMiktar = 0
    aylikSiparisTamamiBedel=0
    aylikSiparisTamamiMiktar = 0
    ay = ""
    background=""
    backgroundSatisSahibi=""
