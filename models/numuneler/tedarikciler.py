from marshmallow import Schema,fields


class NumuneTedarikcichema(Schema):
    id = fields.Int()
    name = fields.String()
   
   

class NumuneTedarikciModel:
    id = None 
    name =""
   