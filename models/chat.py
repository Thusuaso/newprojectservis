from marshmallow import Schema,fields

class ChatSchema(Schema):

    mesaj = fields.String()
    alici = fields.String()
    gonderen = fields.String()
    po = fields.String()

 
class ChatModel:
    mesaj = ""
    alici = ""
    gonderen = ""
    po = ""
    
    