from helpers import SqlConnect
import datetime
from models.raporlar.orderProducts import OrderSchema,OrderModel,MusteriBazindaUretimModel,MusteriBazindaUretimSchema

class Order:
    
    def __init__(self):
        self.data = SqlConnect().data
        
    def getOrderProducts(self,po):
        try:
            siparisUrunresult = self.data.getStoreList("""
                                                select 

                                                su.ID,
                                                (select ur.BirimAdi from UrunBirimTB ur where ur.ID = su.UrunBirimID) as Birim,
                                                su.Miktar,
                                                su.OzelMiktar,
                                                su.Ton,
                                                su.UrunKartID,
                                                (select (select o.En from OlculerTB o where o.ID = urk.OlcuID) from UrunKartTB urk where urk.ID = su.UrunKartID) as En,
                                                (select (select o.Boy from OlculerTB o where o.ID = urk.OlcuID) from UrunKartTB urk where urk.ID = su.UrunKartID) as Boy,
                                                (select (select o.Kenar from OlculerTB o where o.ID = urk.OlcuID) from UrunKartTB urk where urk.ID = su.UrunKartID) as Kenar,
                                                (select (select kt.KategoriAdi from KategoriTB kt where kt.ID=urk.KategoriID) from UrunKartTB urk where urk.ID = su.UrunKartID) as Kategori,
                                                (select (select urun.UrunAdi from UrunlerTB urun where urun.ID=urk.UrunID) from UrunKartTB urk where urk.ID = su.UrunKartID) as UrunAdi,
                                                (select (select yk.YuzeyIslemAdi from YuzeyKenarTB yk where yk.ID=urk.YuzeyID) from UrunKartTB urk where urk.ID = su.UrunKartID) as Yuzey,
                                                (select sum(ur.Miktar) from UretimTB ur where ur.SiparisAciklama = su.SiparisNo and ur.UrunKartID = su.UrunKartID) as UretilenMiktar,
                                                (select sum(ur.Adet) from UretimTB ur where ur.SiparisAciklama = su.SiparisNo and ur.UrunKartID = su.UrunKartID) as UretilenAdet



                                            from 
                                                SiparisUrunTB su
                                                

                                            where 
                                                SiparisNo=?
                                            
                                            
                                            """,po)
            patternKasaMetreKaresi = 0.1239
            setKasaMetreKaresi = 0.011903
            
            liste = list()
            for item in siparisUrunresult:
                model = OrderModel()
                model.id = item.ID
                model.birim = item.Birim
                if item.Birim == 'M2':
                    model.birimBackground = 'yellow'
                elif item.Birim == 'Adet':
                    model.birimBackground = '#98FFA4'
                else:
                    model.birimBackground ='#80ABC5'
                model.miktar = item.Miktar
                model.ozelMiktar = item.OzelMiktar
                model.ton = item.Ton
                model.en = item.En
                model.boy = item.Boy
                model.kenar= item.Kenar
                model.kategori = item.Kategori
                model.urunAdi = item.UrunAdi
                model.yuzey = item.Yuzey
                model.boyut = item.En + 'x' + item.Boy + 'x' + item.Kenar
                if item.UretilenMiktar != None:
                    model.uretimMiktari = item.UretilenMiktar
                    model.kalanMiktar = item.Miktar - item.UretilenMiktar
                    
                                
                    if model.kategori == 'Travertine Mosaic' or model.kategori == 'Marble Mosaic':
                        if model.birim =='M2':
                            model.kalanAdet = float(model.kalanMiktar) / 0.305 / 0.305
                            model.kalanAdet = round(model.kalanAdet)
                    else:
                        
                        if model.birim == 'M2':
                            if model.en == 'ANT':
                                model.kalanAdet = float(model.kalanMiktar) / patternKasaMetreKaresi
                                model.kalanAdet = round(model.kalanAdet)
                                
                            elif model.boy == 'SET':
                                model.kalanMiktar = model.miktar - model.uretimMiktari
                                model.kalanAdet = float(model.kalanMiktar) /  0.07069
                                model.kalanAdet = round(model.kalanAdet)
                            elif model.en == 'SLAB' or model.boy == 'SLAB':
                                model.kalanMiktar = model.miktar - model.uretimMiktari
                                model.kalanAdet = 0
                            elif model.en == 'Free' or model.boy == 'Free' or model.boy == 'FREE' or model.en=='FR':
                                model.kalanMiktar = model.miktar - model.uretimMiktari
                                model.kalanAdet = 0
                            elif model.en == 'VAR' or model.boy == 'VAR':
                                model.kalanMiktar = model.miktar - model.uretimMiktari
                                model.kalanAdet = 0
                            elif model.en == 'Various' or model.boy == 'Various':
                                model.kalanMiktar = model.miktar - model.uretimMiktari
                                model.kalanAdet = 0
                            elif model.en == 'Mini':
                                model.kalanMiktar = model.miktar - model.uretimMiktari
                                model.kalanAdet = 0
                            else:
                                model.kalanAdet = float(model.kalanMiktar) / (self.formatDecimal(model.en) / 100) / (self.formatDecimal(model.boy) / 100)
                                model.kalanAdet = round(model.kalanAdet)
                        elif model.birim == 'Adet':
                            model.kalanAdet = model.miktar - model.uretimMiktari
                    if model.kalanMiktar > 0:
                        model.kalanBilgisi = 'Üretilmesi Gerekiyor'
                        model.kalanRenk = 'red'
                    elif model.kalanMiktar < 0:
                        model.kalanBilgisi = 'Kasa Eksiltilmesi Gerekiyor'
                        model.kalanRenk = 'yellow'
                    else:
                        model.kalanBilgisi='Üretim Tamamlanmıştır'
                        model.kalanRenk = 'green'
                        model.fontColor = 'white'
                else:
                    model.uretimMiktari = 0
                    model.kalanBilgisi = 'Hiç Üretilmemiş'
                    model.kalanRenk = 'black'
                    model.fontColor = 'white'
                    model.kalanMiktar = model.miktar - model.uretimMiktari
                    if model.birim == 'M2':
                        if model.boy == 'Free' or model.boy =='FREE' or model.en=='FR':
                            model.kalanMiktar = model.miktar
                            model.kalanAdet = 0
                        elif model.en == 'Various' or model.boy == 'Various':
                            model.kalanMiktar = model.miktar
                            model.kalanAdet = 0
                        elif model.en == 'ANT':
                            model.kalanMiktar = model.miktar
                            model.kalanAdet = float(model.kalanMiktar) / patternKasaMetreKaresi
                            model.kalanAdet = round(model.kalanAdet)
                        elif model.boy == 'SET':
                            model.kalanMiktar = model.miktar - model.uretimMiktari
                            model.kalanAdet = float(model.kalanMiktar) / 0.07069
                            model.kalanAdet = round(model.kalanAdet)
                        elif model.en == 'SLAB' or model.boy == 'SLAB':
                                model.kalanMiktar = model.miktar - model.uretimMiktari
                                model.kalanAdet = 0
                        elif model.en == 'Mini':
                            model.kalanMiktar = model.miktar - model.uretimMiktari
                            model.kalanAdet = 0
                        elif model.en == 'VAR' or model.boy == 'VAR':
                                model.kalanMiktar = model.miktar - model.uretimMiktari
                                model.kalanAdet = 0
                        elif self.formatDecimal(model.en) <= 10:
                            if model.kategori == 'Travertine Mosaic' or model.kategori == 'Marble Mosaic':
                                model.kalanMiktar = model.miktar
                                model.kalanAdet = float(model.kalanMiktar) / 0.305 / 0.305
                                model.kalanAdet = round(model.kalanAdet)
                        else:
                            model.kalanMiktar = model.miktar
                            model.kalanAdet = float(model.kalanMiktar) / (self.formatDecimal(model.en) / 100) / (self.formatDecimal(model.boy) / 100)
                            model.kalanAdet = round(model.kalanAdet)
                    elif model.birim == 'Adet':
                        model.kalanAdet = model.kalanMiktar
                        
                if item.UretilenAdet != None:
                    model.uretimAdet = item.UretilenAdet
                else:
                    model.uretilenAdet = 0

                liste.append(model)
            schema = OrderSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print("getOrderProducts hata",str(e))
            return False
        
    def formatDecimal(self,value):
        value = value.replace(',','.')
        return float(value)
        
class MusteriBazindaUretim:
    
    def __init__(self):
        self.data = SqlConnect().data
        self.navlun = []
    def getMusteriBazindaUretim(self,yil):
        result = self.data.getStoreList("""
                                            select            
                                                    m.ID as MusteriId,            
                                                    m.FirmaAdi as MusteriAdi,               
                                                    m.Marketing,
                                                    (select yu.UlkeAdi from YeniTeklif_UlkeTB yu where yu.Id = m.UlkeId ) as Ulke,  
                                            (          
                                                Select Sum(SatisToplam) from SiparislerTB s, SiparisUrunTB u where s.SiparisNo=u.SiparisNo and s.SiparisDurumID=2 and s.MusteriID=m.ID and Year(s.SiparisTarihi)=?          
                                                
                                            ) as FOB,
                                            (
                                                select sum(s.NavlunSatis) + sum(DetayTutar_1) + sum(DetayTutar_2) + sum(DetayTutar_3) + sum(DetayTutar_4) from SiparislerTB s where s.SiparisDurumID=2 and s.MusteriID = m.ID and YEAR(s.SiparisTarihi) = ?
                                            ) as CustPaid
                                                from            
                                                MusterilerTB m
                                        
                                        """,(yil,yil))
        liste= list()
        for item in result:
            if(item.FOB == None and item.CustPaid == None):
                continue
            else:
                model = MusteriBazindaUretimModel()
                model.musteriAdi = item.MusteriAdi
                if(item.MusteriId == 37):
                    model.marketing = 'Imperial Homes'
                else:
                    model.marketing = item.Marketing
                model.ulkeAdi = item.Ulke
                model.toplam  = item.FOB
                model.toplamCfr = self.__getNone(item.FOB) + self.__getNone(item.CustPaid)
                liste.append(model)
                
        schema = MusteriBazindaUretimSchema(many=True)
        return schema.dump(liste) 
    
    def getMarketing(self,yil):
        try:
            sipTotal = self.data.getStoreList("""
                                                select 	
                                                sum(su.SatisToplam) as Toplam,
                                                m.Marketing as Marketing
                                            from MusterilerTB m	
                                                inner join SiparislerTB s on s.MusteriID = m.ID
                                                inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo
                                            where 	
                                                    s.SiparisDurumID = 2 and YEAR(s.SiparisTarihi) = ?
                                            group by
                                                m.Marketing
                                            """,(yil))
            self.navlun = self.data.getStoreList("""
                                                    select 	
                                                    sum(s.NavlunSatis) + sum(s.DetayTutar_1) + sum(s.DetayTutar_2) + sum(s.DetayTutar_3) + sum(s.DetayTutar_4) as Navlun,
                                                    m.Marketing as Marketing
                                                from MusterilerTB m	
                                                    inner join SiparislerTB s on s.MusteriID = m.ID
                                                where 	
                                                    s.SiparisDurumID=2 and YEAR(s.SiparisTarihi)=?
                                                group by
                                                    m.Marketing
                                                 
                                                 """,(yil))
            
            liste = list()
            for item in sipTotal:
                model = MusteriBazindaUretimModel()
                model.marketing = item.Marketing
                model.toplam = self.__getNone(item.Toplam)
                model.toplamCfr = item.Toplam + self.__getNone(self.__getNavlunUretim(item.Marketing))
                liste.append(model)
            schema = MusteriBazindaUretimSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getMarketing hata',str(e))
            return False
    
    def __getNavlunUretim(self,marketing):
        for item in self.navlun:
            if item.Marketing != marketing:
                continue
            else:
                return item.Navlun       
    

            
    def __getNone(self,result):
        if(result == None):
            return 0
        else:
            return result   
  