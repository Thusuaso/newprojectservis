from marshmallow import Schema,fields


class SiparisOzetSchema(Schema):

    id = fields.Int()
    ay = fields.Int()
    yil =fields.Int()
    ay_adi = fields.String()
    
    buyil_toplam = fields.Float()
    gecenyil_toplam = fields.Float()
    oncekiyil_toplam = fields.Float()
    
    buyil_mal_bedeli =fields.Float()
    gecenyil_mal_bedeli =fields.Float()
    oncekiyil_mal_bedeli =fields.Float()
    
    fark_yuzde = fields.Float()
    fark = fields.Float()


class SiparisOzetModel:
    id = None 
    ay = 0 
    ay_adi = ""
    yil = 0
    
    buyil_toplam = 0
    gecenyil_toplam = 0
    oncekiyil_toplam = 0
   
    buyil_mal_bedeli = 0
    gecenyil_mal_bedeli = 0
    oncekiyil_mal_bedeli = 0

    fark = 0
    fark_yuzde = 0

class SevkiyatOzetSchema(Schema):

    id = fields.Int()
    ay = fields.Int()
    ay_adi = fields.String()
    
    buyil_toplam = fields.Float()
    gecenyil_toplam = fields.Float()
    oncekiyil_toplam = fields.Float()
    
    buyil_mal_bedeli =fields.Float()
    gecenyil_mal_bedeli =fields.Float()
    oncekiyil_mal_bedeli =fields.Float()
    
    fark_yuzde = fields.Float()
    fark = fields.Float()


class SevkiyatOzetModel:
   
    id = None 
    ay = 0 
    ay_adi = ""
    
    buyil_toplam = 0
    gecenyil_toplam = 0
    oncekiyil_toplam = 0
   
    buyil_mal_bedeli = 0
    gecenyil_mal_bedeli = 0
    oncekiyil_mal_bedeli = 0
   
    fark_yuzde = 0
    fark = 0

class SevSipAyrintiSchema(Schema):

    id = fields.Int()
    tarih = fields.Date()
    siparisnumarasi = fields.String()
    satistoplam = fields.Float()
    detay1 = fields.Float()
    detay2 = fields.Float()
    detay3 = fields.Float()
    detay4 = fields.Float()
    musteri = fields.String()
    navlun = fields.Float()
    yil = fields.Int()
    ay = fields.Int()
    teslim = fields.String()

    
class SevSipAyrintiModel:
    id = None 
    tarih = None
    siparisnumarasi= ""
    satistoplam = 0
    detay1 = 0
    detay2 = 0
    detay3 = 0
    detay4 = 0
    nalun = 0
    musteri = ""
    yil = 0
    ay = 0
    teslim = ""


class SiparisAyrintiSchema(Schema):

     siparisnumarasi = fields.String()
     tarih = fields.Date()
     musteri_id = fields.Int()
     musteri = fields.String()
     tutar = fields.Float()
     yil = fields.Int()
   

    
class SiparisAyrintiModel:

    siparisnumarasi= ""
    tarih = None
    musteri_id = 0
    musteri = ""
    tutar = 0
    yil = 0

class SiparisMusteriAyrintiSchema(Schema):

     siparisnumarasi = fields.String()
     tarih = fields.Date()
     musteri_id = fields.Int()
     musteri = fields.String()
     tutar = fields.Float()
     yil = fields.Int()
     id = fields.Int()
     top = fields.Int()

class SiparisMusteriAyrintiModel:

    siparisnumarasi= ""
    tarih = None
    musteri_id = 0
    musteri = ""
    tutar = 0
    yil = 0 
    id = 0    
    top = 0

class KullaniciSchema(Schema):

     
     musteri_id = fields.Int()
     musteri = fields.String()
     ulkeAdi = fields.String()
     
     sonSiparisTarihi = fields.String()
     logo = fields.String()
     BuYil = fields.Float()
     GecenYil = fields.Float()
     OncekiYil = fields.Float()
     OnDokuzYili = fields.Float()
     OnSekizYili = fields.Float()
     OnYediYili = fields.Float()
     OnAltiYili = fields.Float()
     OnBesYili = fields.Float()
     OnDortYili = fields.Float()
     OnUcYili = fields.Float()
     OnUcYiliOncesi = fields.Float()
     Toplam = fields.Float()
     marketing = fields.String()
     oncelik = fields.String()
     temsilci = fields.String()
     BuYilUretim = fields.Float()
     BuYilSevkiyat = fields.Float()
   

    
class KullaniciModel:

    
    musteri_id = 0
    musteri = ""
    ulkeAdi = ""
    logo = ""
    BuYil = 0
    GecenYil = 0
    OncekiYil = 0
    sonSiparisTarihi = ""
    OnDokuzYili = 0
    OnSekizYili = 0
    OnYediYili = 0
    OnAltiYili = 0
    OnBesYili = 0
    OnDortYili = 0
    OnUcYili = 0
    OnUcYiliOncesi=0
    Toplam = 0 
    marketing = ""
    oncelik = ""
    temsilci = ""
    BuYilUretim = 0
    BuYilSevkiyat = 0
   
class AnasayfaSiparisSchema(Schema):

     
     fobAy = fields.Float()
     FobYil = fields.Float()
     DdpAy = fields.Float()
     DdpYil = fields.Float()
     EfesFobAy = fields.Float()
     EfesFobYil = fields.Float()
     EfesDdpAy = fields.Float()
     EfesDdpYil = fields.Float()
     R3Aylik = fields.Float()
     R4Aylik = fields.Float()
     R7Aylik = fields.Float()
     R8Aylik = fields.Float()
     R14A = fields.Float()
     R14B= fields.Float()

   

    
class AnasayfaSiparisModel:

    
     fobAy = 0
     FobYil = 0
     DdpAy = 0
     DdpYil = 0
     EfesFobAy = 0
     EfesFobYil = 0
     EfesDdpAy = 0
     EfesDdpYil = 0
     R3Aylik = 0
     R4Aylik = 0
     R7Aylik = 0
     R8Aylik = 0
     R14A = 0
     R14B = 0
     
     
     
class SiparisBazindaOzetSchema(Schema):
    
    aylar = fields.Integer()
    fob = fields.Integer()
    ddp = fields.Integer()
    fark = fields.Integer()
    
    
class SiparisBazindaOzetModel():
    aylar = 0
    fob = 0
    ddp = 0
    fark = 0
    
    
class CustomersDetailListShema(Schema):
    satisFiyati = fields.Float()
    satisToplam = fields.Float()
    miktar = fields.Float()
    birimAdi = fields.String()
    kategori = fields.String()
    urunAdi = fields.String()
    yuzey = fields.String()
    en = fields.String()
    boy = fields.String()
    kenar = fields.String()
    
class CustomersDetailListModel:
    satisFiyati = 0
    satisToplam = 0
    miktar = 0
    birimAdi = ''
    kategori = ''
    urunAdi = ''
    yuzey = ''
    en = ''
    boy = ''
    kenar = ''