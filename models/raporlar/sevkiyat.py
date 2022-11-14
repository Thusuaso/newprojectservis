from marshmallow import fields
from models.raporlar.uretim import UretimSchema,UretimModel


class SevkiyatSchema(UretimSchema):
    kutuadet = fields.Int()
    birimfiyat = fields.Float()
    toplam = fields.Float()
    musteriadi = fields.String()

class SevkiyatModel(UretimModel):
    kutuadet = 0
    birimfiyat = 0
    toplam = 0
    musteriadi = ""

model = SevkiyatModel()

