from marshmallow import Schema,fields


class GalleriaPhotosSchema(Schema):
    id = fields.Int()
    image_link = fields.String()
    product_id = fields.Int()
    file_name = fields.String()
    videos_control = fields.Boolean()

class GalleriaPhotosModel:

    id = 0
    image_link = ""
    product_id = 0
    file_name = ""
    videos_control:0