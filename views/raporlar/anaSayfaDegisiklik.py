from helpers import SqlConnect
from models.raporlar.anaSayfaDegisiklik import UretimUrunlerModel,UretimUrunlerSchema

        
class UretimUrunler:
    def __init__(self):
        self.data = SqlConnect().data
        
    def getUretimUrunlerListesi(self):
        try:
            result = self.data.getList("""
                                        select 
	
                                            sum(su.Miktar) SipMiktar,
                                            su.UrunKartID,
                                            (select sum(u.Miktar) From UretimTB u where u.UrunKartID = su.UrunKartID and u.UrunDurumID=1) as UretimMiktar,
                                            (select (select kt.KategoriAdi from KategoriTB kt where kt.ID=uk.KategoriID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kategori,
                                            (sum(su.Miktar) - (select sum(u.Miktar) From UretimTB u where u.UrunKartID = su.UrunKartID and u.UrunDurumID=1)) as UretilmesiGereken,
                                            (select (select urn.UrunAdi from UrunlerTB urn where urn.ID=uk.UrunID) from UrunKartTB uk where uk.ID = su.UrunKartID) as UrunBilgisi,
                                            (select (select yk.YuzeyIslemAdi from YuzeyKenarTB yk where yk.ID=uk.YuzeyID) from UrunKartTB uk where uk.ID = su.UrunKartID) as YuzeyIslem,
                                            (select (select ol.En from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as En,
                                            (select (select ol.Boy from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Boy,
                                            (select (select ol.Kenar from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kenar

                                        from 
                                            SiparislerTB sp
                                            inner join SiparisUrunTB su on su.SiparisNo = sp.SiparisNo

                                        where 
                                            sp.SiparisDurumID = 2
                                            
                                        group by
                                            su.UrunKartID
                                        
                                        order by En
                                        
                                       
                                       
                                       """)
            
            liste = list()
            for item in result:
                model = UretimUrunlerModel()
                model.kategori = item.Kategori
                model.urunAdi = item.UrunBilgisi
                model.yuzey = item.YuzeyIslem
                model.en = item.En
                model.boy = item.Boy
                model.kenar = item.Kenar
                model.sipMiktari = item.SipMiktar
                model.urunKartId = item.UrunKartID
                if item.UretimMiktar == None:
                    model.uretimMiktar = 0
                    model.uretilmesiGereken = model.sipMiktari - model.uretimMiktar
                else:
                    model.uretimMiktar = item.UretimMiktar
                    
                    model.uretilmesiGereken = item.UretilmesiGereken
                if model.sipMiktari == model.uretimMiktar:
                    model.background = '#66ff66'
                elif model.uretimMiktar == 0:
                    model.background = '#f44336'
                elif model.uretilmesiGereken < 0:
                    model.background = "yellow"
                elif model.uretilmesiGereken > 0:
                    model.background = "#c6e2ff"
                liste.append(model)
            schema = UretimUrunlerSchema(many=True)
            return schema.dump(liste)
            
            
            
        except Exception as e:
            print("getUretimUrunlerListesi",str(e))
            return False
        
    def getUretimUrunlerAyrintiListesi(self,urunKartId):
        try:
            result = self.data.getStoreList("""
                                        select 
                                            su.SiparisNo,
                                            su.Miktar as SipMiktar,
                                            su.UrunKartID,
                                            (select (select kt.KategoriAdi from KategoriTB kt where kt.ID=uk.KategoriID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kategori,
                                            (select (select urn.UrunAdi from UrunlerTB urn where urn.ID=uk.UrunID) from UrunKartTB uk where uk.ID = su.UrunKartID) as UrunBilgisi,
                                            (select (select yk.YuzeyIslemAdi from YuzeyKenarTB yk where yk.ID=uk.YuzeyID) from UrunKartTB uk where uk.ID = su.UrunKartID) as YuzeyIslem,
                                            (select (select ol.En from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as En,
                                            (select (select ol.Boy from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Boy,
                                            (select (select ol.Kenar from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kenar

                                        from 
                                            SiparislerTB sp
                                            inner join SiparisUrunTB su on su.SiparisNo = sp.SiparisNo

                                        where 
                                            sp.SiparisDurumID = 2 and su.UrunKartID=?
                                                                                
                                        order by En
                                   
                                   """,urunKartId)
            liste = list()
            for item in result :
                model = UretimUrunlerModel()
                model.siparisNo = item.SiparisNo
                model.kategori = item.Kategori
                model.urunAdi = item.UrunBilgisi
                model.yuzey = item.YuzeyIslem
                model.en = item.En
                model.boy = item.Boy
                model.kenar = item.Kenar
                model.sipMiktari = item.SipMiktar
                liste.append(model)
            schema = UretimUrunlerSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print("getUretimUrunlerAyrintiListesi hata",str(e))
            return False
        
    def getUretimUrunlerListesiMekmar(self):
        try:
            result = self.data.getList("""
                                        select 
	
                                            sum(su.Miktar) SipMiktar,
                                            su.UrunKartID,
                                            (select sum(u.Miktar) From UretimTB u where u.UrunKartID = su.UrunKartID and u.UrunDurumID=1) as UretimMiktar,
                                            (select (select kt.KategoriAdi from KategoriTB kt where kt.ID=uk.KategoriID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kategori,
                                            (sum(su.Miktar) - (select sum(u.Miktar) From UretimTB u where u.UrunKartID = su.UrunKartID and u.UrunDurumID=1)) as UretilmesiGereken,
                                            (select (select urn.UrunAdi from UrunlerTB urn where urn.ID=uk.UrunID) from UrunKartTB uk where uk.ID = su.UrunKartID) as UrunBilgisi,
                                            (select (select yk.YuzeyIslemAdi from YuzeyKenarTB yk where yk.ID=uk.YuzeyID) from UrunKartTB uk where uk.ID = su.UrunKartID) as YuzeyIslem,
                                            (select (select ol.En from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as En,
                                            (select (select ol.Boy from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Boy,
                                            (select (select ol.Kenar from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kenar

                                        from 
                                            SiparislerTB sp
                                            inner join SiparisUrunTB su on su.SiparisNo = sp.SiparisNo
											inner join MusterilerTB m on m.ID = sp.MusteriID

                                        where 
                                            sp.SiparisDurumID = 2 and m.Marketing ='Mekmar'
                                        group by
                                            su.UrunKartID
                                        order by En
                                        
                                       
                                       
                                       """)
            
            liste = list()
            for item in result:
                model = UretimUrunlerModel()
                model.kategori = item.Kategori
                model.urunAdi = item.UrunBilgisi
                model.yuzey = item.YuzeyIslem
                model.en = item.En
                model.boy = item.Boy
                model.kenar = item.Kenar
                model.sipMiktari = item.SipMiktar
                model.urunKartId = item.UrunKartID
                if item.UretimMiktar == None:
                    model.uretimMiktar = 0
                    model.uretilmesiGereken = model.sipMiktari - model.uretimMiktar
                else:
                    model.uretimMiktar = item.UretimMiktar
                    
                    model.uretilmesiGereken = item.UretilmesiGereken
                if model.sipMiktari == model.uretimMiktar:
                    model.background = '#66ff66'
                elif model.uretimMiktar == 0:
                    model.background = '#f44336'
                elif model.uretilmesiGereken < 0:
                    model.background = "yellow"
                elif model.uretilmesiGereken > 0:
                    model.background = "#c6e2ff"
                liste.append(model)
            schema = UretimUrunlerSchema(many=True)
            return schema.dump(liste)
            
            
            
        except Exception as e:
            print("getUretimUrunlerListesi",str(e))
            return False
       
    def getUretimUrunlerAyrintiListesiMekmar(self,urunKartId):
        try:
            result = self.data.getStoreList("""
                                        select 
                                            su.SiparisNo,
                                            su.Miktar as SipMiktar,
                                            su.UrunKartID,
                                            (select (select kt.KategoriAdi from KategoriTB kt where kt.ID=uk.KategoriID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kategori,
                                            (select (select urn.UrunAdi from UrunlerTB urn where urn.ID=uk.UrunID) from UrunKartTB uk where uk.ID = su.UrunKartID) as UrunBilgisi,
                                            (select (select yk.YuzeyIslemAdi from YuzeyKenarTB yk where yk.ID=uk.YuzeyID) from UrunKartTB uk where uk.ID = su.UrunKartID) as YuzeyIslem,
                                            (select (select ol.En from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as En,
                                            (select (select ol.Boy from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Boy,
                                            (select (select ol.Kenar from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kenar

                                        from 
                                            SiparislerTB sp
                                            inner join SiparisUrunTB su on su.SiparisNo = sp.SiparisNo
                                            inner join MusterilerTB m on m.ID = sp.MusteriID

                                        where 
                                            sp.SiparisDurumID = 2 and su.UrunKartID=? and m.Marketing ='Mekmar'
                                                                                
                                        order by En
                                   
                                   """,urunKartId)
            liste = list()
            for item in result :
                model = UretimUrunlerModel()
                model.siparisNo = item.SiparisNo
                model.kategori = item.Kategori
                model.urunAdi = item.UrunBilgisi
                model.yuzey = item.YuzeyIslem
                model.en = item.En
                model.boy = item.Boy
                model.kenar = item.Kenar
                model.sipMiktari = item.SipMiktar
                liste.append(model)
            schema = UretimUrunlerSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print("getUretimUrunlerAyrintiListesi hata",str(e))
            return False
        
       
       
    def getUretimUrunlerListesiMekmer(self):
        try:
            result = self.data.getList("""
                                        select 
	
                                            sum(su.Miktar) SipMiktar,
                                            su.UrunKartID,
                                            (select sum(u.Miktar) From UretimTB u where u.UrunKartID = su.UrunKartID and u.UrunDurumID=1) as UretimMiktar,
                                            (select (select kt.KategoriAdi from KategoriTB kt where kt.ID=uk.KategoriID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kategori,
                                            (sum(su.Miktar) - (select sum(u.Miktar) From UretimTB u where u.UrunKartID = su.UrunKartID and u.UrunDurumID=1)) as UretilmesiGereken,
                                            (select (select urn.UrunAdi from UrunlerTB urn where urn.ID=uk.UrunID) from UrunKartTB uk where uk.ID = su.UrunKartID) as UrunBilgisi,
                                            (select (select yk.YuzeyIslemAdi from YuzeyKenarTB yk where yk.ID=uk.YuzeyID) from UrunKartTB uk where uk.ID = su.UrunKartID) as YuzeyIslem,
                                            (select (select ol.En from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as En,
                                            (select (select ol.Boy from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Boy,
                                            (select (select ol.Kenar from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kenar

                                        from 
                                            SiparislerTB sp
                                            inner join SiparisUrunTB su on su.SiparisNo = sp.SiparisNo
											inner join MusterilerTB m on m.ID = sp.MusteriID

                                        where 
                                            sp.SiparisDurumID = 2 and m.Marketing in ('Mekmer', 'İç Piyasa')
                                        group by
                                            su.UrunKartID
                                        order by En
                                        
                                       
                                       
                                       """)
            
            liste = list()
            for item in result:
                model = UretimUrunlerModel()
                model.kategori = item.Kategori
                model.urunAdi = item.UrunBilgisi
                model.yuzey = item.YuzeyIslem
                model.en = item.En
                model.boy = item.Boy
                model.kenar = item.Kenar
                model.sipMiktari = item.SipMiktar
                model.urunKartId = item.UrunKartID
                if item.UretimMiktar == None:
                    model.uretimMiktar = 0
                    model.uretilmesiGereken = model.sipMiktari - model.uretimMiktar
                else:
                    model.uretimMiktar = item.UretimMiktar
                    
                    model.uretilmesiGereken = item.UretilmesiGereken
                if model.sipMiktari == model.uretimMiktar:
                    model.background = '#66ff66'
                elif model.uretimMiktar == 0:
                    model.background = '#f44336'
                elif model.uretilmesiGereken < 0:
                    model.background = "yellow"
                elif model.uretilmesiGereken > 0:
                    model.background = "#c6e2ff"
                liste.append(model)
            schema = UretimUrunlerSchema(many=True)
            return schema.dump(liste)
            
            
            
        except Exception as e:
            print("getUretimUrunlerListesi",str(e))
            return False
       
    def getUretimUrunlerAyrintiListesiMekmer(self,urunKartId):
        try:
            result = self.data.getStoreList("""
                                        select 
                                            su.SiparisNo,
                                            su.Miktar as SipMiktar,
                                            su.UrunKartID,
                                            (select (select kt.KategoriAdi from KategoriTB kt where kt.ID=uk.KategoriID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kategori,
                                            (select (select urn.UrunAdi from UrunlerTB urn where urn.ID=uk.UrunID) from UrunKartTB uk where uk.ID = su.UrunKartID) as UrunBilgisi,
                                            (select (select yk.YuzeyIslemAdi from YuzeyKenarTB yk where yk.ID=uk.YuzeyID) from UrunKartTB uk where uk.ID = su.UrunKartID) as YuzeyIslem,
                                            (select (select ol.En from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as En,
                                            (select (select ol.Boy from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Boy,
                                            (select (select ol.Kenar from OlculerTB ol where ol.ID=uk.OlcuID) from UrunKartTB uk where uk.ID = su.UrunKartID) as Kenar

                                        from 
                                            SiparislerTB sp
                                            inner join SiparisUrunTB su on su.SiparisNo = sp.SiparisNo
                                            inner join MusterilerTB m on m.ID = sp.MusteriID

                                        where 
                                            sp.SiparisDurumID = 2 and su.UrunKartID=? and m.Marketing in ('Mekmer', 'İç Piyasa')
                                                                                
                                        order by En
                                   
                                   """,urunKartId)
            liste = list()
            for item in result :
                model = UretimUrunlerModel()
                model.siparisNo = item.SiparisNo
                model.kategori = item.Kategori
                model.urunAdi = item.UrunBilgisi
                model.yuzey = item.YuzeyIslem
                model.en = item.En
                model.boy = item.Boy
                model.kenar = item.Kenar
                model.sipMiktari = item.SipMiktar
                liste.append(model)
            schema = UretimUrunlerSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print("getUretimUrunlerAyrintiListesi hata",str(e))
            return False
       