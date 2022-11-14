from marshmallow import Schema,fields



class CardListSchema(Schema):
    id = fields.Int()
    name = fields.String()

class CardListModel:
    id = None 
    name = ""