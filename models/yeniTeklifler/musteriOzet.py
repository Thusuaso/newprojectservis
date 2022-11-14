from marshmallow import fields
from models.yeniTeklifler import HatirlatmaModel,HatirlatmaSchema


class MusteriOzetSchema(HatirlatmaSchema):
    kullaniciAdi = fields.String()
    teklifSayisi = fields.Int()


class MusteriOzetModel(HatirlatmaModel):
    kullaniciAdi = ""
    teklifSayisi = 0