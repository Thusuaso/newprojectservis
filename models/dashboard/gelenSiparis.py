from marshmallow import Schema,fields


class GelenSiparisSchema(Schema):
    siparisSahibi = fields.Int()
    gelenSiparisFob = fields.Float()
    gelenSiparisAy = fields.String()
    gelenSiparisYil = fields.Int()
    gelenSiparisAylikOrtalama = fields.Float()
    gelenSiparisYilSonuTahmini = fields.Float()
    
class GelenSiparisModel:
    siparisSahibi = 0
    gelenSiparisFob = 0
    gelenSiparisAy = ""
    gelenSiparisYil=0
    gelenSiparisAylikOrtalama = 0
    gelenSiparisYilSonuTahmini = 0


class SiparislerKonteynirSchema(Schema):
    firmaAdi = fields.String()
    siparisNo = fields.String()
    line = fields.String()
    yuklemeTarihi = fields.String()
    siparisTarihi = fields.String()
    konteynirNo = fields.String()
    etaTarihi = fields.String()
    navlunFirma = fields.String()
    kalan = fields.Float()
class SiparislerKonteynirModel:
    firmaAdi = ""
    siparisNo = ""
    line = ""
    yuklemeTarihi = ""
    siparisTarihi = ""
    konteynirNo = ""
    etaTarihi = ""
    navlunFirma = ""
    kalan = 0
    
class FinansTakipListesiSchema(Schema):
    musteriAdi = fields.String()
    siparisNo = fields.String()
    siparisDurum = fields.String()
    odenen = fields.Float()
    satisToplami = fields.Float()
    siparisSahibi = fields.String()
    operasyon = fields.String()
    kalanBedel = fields.Float()

class FinansTakipListesiModel:
    musteriAdi = ""
    siparisNo = ""
    siparisDurum = ""
    odenen = 0
    satisToplami = 0
    siparisSahibi = ""
    operasyon = ""
    kalanBedel = 0

class TedarikciListesiSchema(Schema):
    satisToplam = fields.Float()
    satisMiktar = fields.Float()
    tedarikci = fields.String()
    tedarikci_id = fields.Int()
    firmaId = fields.Int()
class TedarikciListesiModel:
    satisToplam = 0
    satisMiktar = 0
    tedarikci = ""
    tedarikci_id = 0
    firmaId = 0
class TeklifListesiSchema(Schema):
    teklifSahibi = fields.String()
    teklifSayisi = fields.Int()
    teklifSahibiId = fields.Int()
class TeklifListesiModel:
    teklifSahibi = ""
    teklifSayisi = 0
    teklifSahibiId=0

class SonEklenenSiparislerSchema(Schema):
    satisToplami = fields.Float()
    siparisNo = fields.String()
    satisci = fields.String()
    link = fields.String()
    evrakDurum = fields.Boolean()
class SonEklenenSiparislerModel:
    satisToplami = 0
    siparisNo = ""
    satisci = ""
    link = ""
    evrakDurum = 0
    
class TedarikciAyrintiSchema(Schema):
    siparisNo = fields.String()
    satisMiktari = fields.Float()
    firmaAdi = fields.String()
    satisToplami = fields.Float()
    
class TedarikciAyrintiModel:
    siparisNo = ""
    satisMiktari = 0
    firmaAdi = ""
    satisToplami = ""
    
class FirmaBazindaAyrintiSchema(Schema):
    siparisNo = fields.String()
    satisToplami = fields.Float()
    satisMiktari = fields.Float()
    
class FirmaBazindaAyrintiModel:
    siparisNo=""
    satisToplami = 0
    satisMiktari=0
    
class TeklifAyrintiSchema(Schema):
    tarih = fields.String()
    musteri = fields.String()
    kaynakYeri = fields.String()
    aciklama = fields.String()

class TeklifAyrintiModel:
    tarih = ""
    musteri = ""
    kaynakYeri = ""
    aciklama = ""
    
class TeklifUlkeyeGoreSchema(Schema):
    ulkeAdi = fields.String()
    topTeklif = fields.Int()
    ulkeId = fields.Int()
    
class TeklifUlkeyeGoreModel:
    ulkeAdi = ""
    topTeklif = 0
    ulkeId = 0
    
class TeklifUlkeyeGoreAyrintiSchema(Schema):
    teklifId = fields.Int()
    teklifNo = fields.Int()
    tarih = fields.String()
    kullaniciAdi = fields.String()
    musteriAdi = fields.String()
    kategoriAdi = fields.String()
    urunAdi = fields.String()
    kalinlik = fields.String()
    enBoy = fields.String()
    islemAdi = fields.String()
    fobFiyat = fields.Float()
    teklifFiyat = fields.Float()
    birim = fields.String()
    
class TeklifUlkeyeGoreAyrintiModel:
    teklifId = 0
    teklifNo = 0
    tarih = ''
    kullaniciAdi = ''
    musteriAdi = ''
    kategoriAdi = ''
    urunAdi = ''
    kalinlik = ''
    enBoy = ''
    islemAdi = ''
    fobFiyat = 0
    teklifFiyat = 0
    birim = ''
    
    
class TahminiDegisiklikSchema(Schema):
    degisiklik = fields.String()
    degisiklikAlani = fields.String()
    year = fields.String()
    month = fields.String()
    day = fields.String()
    watch = fields.String()
class TahminiDegisiklikModel:
    degisiklik = ""
    degisiklikAlani = ""
    year = ""
    month = ""
    day = ""
    watch = ""