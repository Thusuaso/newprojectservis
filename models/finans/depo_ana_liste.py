from marshmallow import Schema,fields


class DepoAnaListeSchema(Schema):
    id = fields.Int()
    musteriadi = fields.String()
    ciro = fields.Float()
    odenen = fields.Float()
    bakiye = fields.Float()

class DepoAnaListeModel:
    id = None
    musteriadi = ""
    ciro = 0
    odenen = 0
    bakiye = 0