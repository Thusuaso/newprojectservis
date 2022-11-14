from marshmallow import Schema,fields

class CeyreklikRaporlarSchema(Schema):
    ay = fields.Int()
    ayStr = fields.String()
    ekTutarlar = fields.Float()
    masraflar = fields.Float()
    navlunSatis = fields.Float()
    navlunAlis = fields.Float()
    satisToplami = fields.Float()
    genelToplam = fields.Float()
class CeyreklikRaporlarModel:
    ay = 0
    ayStr = ""
    ekTutarlar = 0
    masraflar = 0
    navlunSatis = 0
    navlunAlis = 0
    satisToplami = 0
    genelToplam = 0
    
class QuartersDataStatisticsSchema(Schema):
    medyanOne = fields.Float()
    stdOne = fields.Float()
    varyansOne = fields.Float()
    ortalamaOne = fields.Float()
    yuzdeOne = fields.Float()
    
    medyanTwo= fields.Float()
    stdTwo = fields.Float()
    varyansTwo = fields.Float()
    ortalamaTwo = fields.Float()
    yuzdeTwo = fields.Float()
    
    
    medyanThree = fields.Float()
    stdThree = fields.Float()
    varyansThree = fields.Float()
    ortalamaThree = fields.Float()
    yuzdeThree = fields.Float()
    
    
    medyanFour = fields.Float()
    stdFour = fields.Float()
    varyansFour = fields.Float()
    ortalamaFour = fields.Float()
    yuzdeFour = fields.Float()
    
    
    
class QuartersDataStatisticsModel:
    medyanOne = 0
    stdOne = 0
    varyansOne = 0
    ortalamaOne = 0
    yuzdeOne = 0
    
    medyanTwo = 0
    stdTwo = 0
    varyansTwo = 0
    ortalamaTwo = 0
    yuzdeTwo = 0
    
    medyanThree = 0
    stdThree = 0
    varyansThree = 0
    ortalamaThree = 0
    yuzdeThree = 0
    
    medyanFour = 0
    stdFour = 0
    varyansFour = 0
    ortalamaFour = 0
    yuzdeFour = 0
    