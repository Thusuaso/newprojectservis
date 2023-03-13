from helpers import SqlConnect
from models.raporlar.stokraporu import StokRaporuFilterModel,StokRaporuFilterSchema 
class StokListFilter:
    def __init__(self):
        self.data = SqlConnect().data
        self.urunler = self.data.getList("""
                                            select 

                                                    count(u.UrunKartID) as KasaSayisi,
                                                    uk.UrunId as UrunId,
													(select urun.UrunAdi from UrunlerTB urun where urun.ID = uk.UrunID) as UrunAdi,
													sum(u.Miktar) as Miktar
                                                    
                                                    


                                            from UretimTB u 
                                                inner join UrunKartTB uk on uk.ID = u.UrunKartID

                                            where u.UrunDurumID = 1 and u.Bulunamadi != 1
                                            group by uk.UrunID
                                            order by sum(u.Miktar) desc
                                         
                                         
                                         
                                         """)
        self.yuzeyler = self.data.getList("""
                                            select 

                                                uk.UrunID as UrunID,
                                                count(uk.YuzeyID) as YuzeySayisi,
												yk.ID as YuzeyId,
												yk.YuzeyIslemAdi as YuzeyIslemAdi,
												sum(u.Miktar) as Miktar

												

                                            from UretimTB u
                                                inner join UrunKartTB uk on uk.ID = u.UrunKartID
												inner join YuzeyKenarTB yk on yk.ID = uk.YuzeyID

                                            where u.UrunDurumID=1 and u.Bulunamadi != 1
                                            group by uk.UrunID,yk.ID,yk.YuzeyIslemAdi
											order by uk.UrunID
                                          
                                          """)
        self.ebatlar = self.data.getList("""
                                                select 

                                                    urun.ID as UrunId,
                                                    yk.ID as YuzeyId,
                                                    o.ID as OlculerId,
                                                    sum(u.Miktar) as Miktar,
                                                    count(u.ID) as KasaSayisi,
                                                    o.En as En,
                                                    o.Boy as Boy,
                                                    o.Kenar as Kenar,
                                                    u.UrunKartID as UrunKartID


                                                from UretimTB u
                                                inner join UrunKartTB uk on uk.ID = u.UrunKartID
                                                inner join UrunlerTB urun on urun.ID = uk.UrunID
                                                inner join YuzeyKenarTB yk on yk.ID = uk.YuzeyID
                                                inner join OlculerTB o on o.ID = uk.OlcuID

                                                where u.UrunDurumID = 1 and u.Bulunamadi != 1

                                                group by
                                                    urun.ID,yk.ID,o.ID,o.En,o.Boy,o.Kenar,u.UrunKartID
                                                order by urun.ID
                                         
                                         """)
 
    def getStokListFilter(self):
        liste = list()
        urunlerKey = 0
        for item in self.urunler:
            liste.append({
                'key':urunlerKey,
                'data':{
                        'label':item.UrunAdi,
                    'kasaSayisi':item.KasaSayisi,
                    'miktar':float(item.Miktar)
            },
                
                'children':self.__yuzeyler(urunlerKey,item.UrunId)
            })
            
            urunlerKey += 1
            
        return liste
            
    def __yuzeyler(self,urunlerKey,UrunID):
        liste = list()
        yuzeylerKey = 0
        for item in self.yuzeyler:
            if(item.UrunID == UrunID):
                liste.append({
                    'key': str(urunlerKey) + '-'  + str(yuzeylerKey),
                    'data':{
                            'label':item.YuzeyIslemAdi,
                    'kasaSayisi':item.YuzeySayisi,
                    'miktar':float(item.Miktar)
                    },
                    
                    'children':self.__ebatlar(urunlerKey,yuzeylerKey,UrunID,item.YuzeyId)
                })
                yuzeylerKey += 1
                
        return liste
    
    def __ebatlar(self,urunlerKey,yuzeylerKey,urunId,yuzeyId):
        liste = list()
        ebatlarKey = 0
        for item in self.ebatlar:
            if(item.UrunId == urunId):
                if(item.YuzeyId ==yuzeyId):
                    liste.append({
                        'key':str(urunlerKey) + '-' + str(yuzeylerKey) + '-' + str(ebatlarKey),
                        'data':{
                            'label':str(item.En) + 'x' + str(item.Boy) + 'x' + str(item.Kenar),
                        'kasaSayisi':item.KasaSayisi,
                        'miktar':float(item.Miktar),
                        'urunId':item.UrunId,
                        'yuzeyId':item.YuzeyId,
                        'olculerId':item.OlculerId,
                        'urunKartId':item.UrunKartID
                        }
                        
                    })

                    ebatlarKey += 1
                
        return liste
    
    def getStokListFilterAyrinti(self,urunKartId):
        try:
            result = self.data.getStoreList("""
                                                select 

                                                    u.KasaNo as KasaNo,
                                                    u.Tarih as Tarih,
                                                    k.KategoriAdi,
                                                    urun.UrunAdi,
                                                    yk.YuzeyIslemAdi,
                                                    o.En + 'x' + o.Boy + 'x' + o.Kenar as Olcu,
                                                    t.FirmaAdi,
                                                    ocak.OcakAdi,
                                                    ud.UrunDurum,
                                                    u.SiparisAciklama,
                                                    u.Aciklama,
                                                    u.Miktar,
                                                    ub.BirimAdi,
                                                    u.KutuAdet,
                                                    u.KutuIciAdet,
                                                    u.Adet

                                                    


                                                from UretimTB u
                                                    inner join UrunKartTB uk on uk.ID = u.UrunKartID
                                                    inner join KategoriTB k on k.ID = uk.KategoriID
                                                    inner join UrunlerTB urun on urun.ID = uk.UrunID
                                                    inner join YuzeyKenarTB yk on yk.ID = uk.YuzeyID
                                                    inner join OlculerTB o on o.ID = uk.OlcuID
                                                    inner join TedarikciTB t on t.ID = u.TedarikciID
                                                    inner join UrunOcakTB ocak on ocak.ID = u.UrunOcakID
                                                    inner join UrunBirimTB ub on ub.ID = u.UrunBirimID
                                                    inner join UrunDurumTB ud on ud.ID = u.UrunDurumID

                                                where
                                                    u.UrunDurumID=1 and u.Bulunamadi != 1 and u.UrunKartID =? 
                                            
                                            """,(urunKartId))
            
            liste =list()
            sira = 1
            for item in result:
                model = StokRaporuFilterModel()
                model.sira = sira
                model.kasa_no = item.KasaNo
                model.tarih = item.Tarih
                model.kategori_adi = item.KategoriAdi
                model.urun_adi = item.UrunAdi
                model.yuzey_islem = item.YuzeyIslemAdi
                model.olcu = item.Olcu
                model.firma_adi = item.FirmaAdi
                model.ocak_adi = item.OcakAdi
                model.urun_durum = item.UrunDurum
                model.siparis_aciklama = item.SiparisAciklama
                model.aciklama = item.Aciklama
                model.miktar = item.Miktar
                model.birim_adi = item.BirimAdi
                model.kutu_adet = item.KutuAdet
                model.kutu_ici_adet = item.KutuIciAdet
                model.adet = item.Adet
                liste.append(model)
                sira += 1
            schema = StokRaporuFilterSchema(many=True)
            return schema.dump(liste)
        
        except Exception as e:
            print('getStokListFilterAyrinti hata',str(e))
            return False
                
            