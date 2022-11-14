from marshmallow import fields,Schema


class SiparisGiderTurSchema(Schema):

    id = fields.Int()
    giderTur = fields.String() 


class SiparisGiderTurModel:
    id = None 
    giderTur = ""