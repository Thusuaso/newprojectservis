from marshmallow import Schema,fields


class GenelListSchema(Schema):
    id = fields.Int()
    name = fields.String()


class GenelListModel:
    id = None 
    name = ""

    
class GenelKategoriListSchema(Schema):
    id = fields.Int()
    kategoriAdi = fields.String()


class GenelKategoriListModel:
    id = None 
    kategoriAdi = ""