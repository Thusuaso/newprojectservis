from helpers import SqlConnect
from models.raporlar.mkraporlar.raporlar import *
class MkRaporlar:
    def __init__(self):
        self.sql = SqlConnect().data
        self.yuklenenMusteriMasraf = []
        self.yuklenenPo = []
        self.yuklenenPoMasraf = []
    def mkRaporlarSevkSip(self,yil):
        try:
            data = self.sql.getStoreList("""
                                    select 
                                        m.FirmaAdi,

                                        (
                                            select sum(su.SatisToplam) from SiparislerTB s, SiparisUrunTB su where  s.MusteriID = m.ID and s.SiparisNo = su.SiparisNo and YEAR(s.SiparisTarihi) = ?
                                        ) as BuYilSiparisler,
                                        (
                                            select sum(su.SatisToplam) from SiparislerTB s, SiparisUrunTB su where s.MusteriID = m.ID and s.SiparisNo = su.SiparisNo and YEAR(s.YuklemeTarihi) = ?
                                        ) as BuYilYuklenenler

                                    from MusterilerTB m
                                    where m.Marketing = 'Mekmar'
                                  
                                  """,(yil,yil))
            self.yuklenenMusteriMasraf = self.sql.getStoreList("""
                                                    select
                                                        m.FirmaAdi,
                                                        sum(s.NavlunSatis) + sum(s.DetayTutar_1) + sum(s.DetayTutar_2) + sum(s.DetayTutar_3) as NavlunvDiger

                                                    from SiparislerTB s
                                                        inner join MusterilerTB m on m.ID = s.MusteriID
                                                    where
                                                        YEAR(s.YuklemeTarihi) = ? and m.Marketing = 'Mekmar'
                                                    group by s.MusteriID,m.FirmaAdi
                                                  """,(yil))
            fullyListe = list()
            for item2 in data:
                if(item2.BuYilSiparisler == None and item2.BuYilYuklenenler == None):
                    continue
                else:
                    fullyListe.append(item2)

            liste = list()
            for item in fullyListe:
                model = MkRaporlarSevkSipModel()
                model.siparisfob = self.__noneControl(item.BuYilSiparisler)
                model.yuklenenfob = self.__noneControl(item.BuYilYuklenenler)
                model.yuklenenddp = model.yuklenenfob + self.__noneControl(self.__getYuklenenMasraf(item.FirmaAdi))
                model.musteriadi = item.FirmaAdi
                liste.append(model)
            schema = MkRaporlarSevkSipSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('mkRaporlarSevkSip hata',str(e))
            return False
    
    def mkRaporlarSevkSipPo(self,yil):
        try:
            data = self.sql.getStoreList("""
                                    select 
                                        m.FirmaAdi,
                                        s.SiparisNo,
                                        sum(su.SatisToplam) as SatisToplam,
										s.SiparisTarihi,
                                        (select stt.TeslimTur from SiparisTeslimTurTB stt where stt.ID = s.TeslimTurID) as TeslimTur
                                    from SiparislerTB s
                                        inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo
                                        inner join MusterilerTB m on m.ID = s.MusteriID
                                    where
                                        YEAR(s.SiparisTarihi) = ? and m.Marketing = 'Mekmar'

                                    group by
                                        s.SiparisNo,m.FirmaAdi,s.SiparisTarihi,s.TeslimTurID

									order by
										s.SiparisTarihi
                                  
                                  """,(yil))
            self.yuklenenPo = self.sql.getStoreList("""
                                                    select 
                                                        m.FirmaAdi,
                                                        s.SiparisNo,
                                                        sum(su.SatisToplam) as SatisToplam,
                                                        s.SiparisTarihi,
                                                        s.YuklemeTarihi

                                                    from SiparislerTB s
                                                        inner join SiparisUrunTB su on su.SiparisNo = s.SiparisNo
                                                        inner join MusterilerTB m on m.ID = s.MusteriID
                                                    where
                                                        YEAR(s.YuklemeTarihi) = ? and m.Marketing = 'Mekmar'

                                                    group by
                                                        s.SiparisNo,m.FirmaAdi,s.SiparisTarihi,s.YuklemeTarihi

                                                    order by
                                                        s.YuklemeTarihi
                                                  """,(yil))
            self.yuklenenPoMasraf = self.sql.getStoreList("""
                                                            select 
                                                                s.SiparisNo,
                                                                s.NavlunSatis + s.DetayTutar_1 + s.DetayTutar_2 + s.DetayTutar_3 as Masraflar

                                                            from SiparislerTB s
                                                                inner join MusterilerTB m on m.ID = s.MusteriID

                                                            where YEAR(s.YuklemeTarihi) = ? and m.Marketing='Mekmar'
                                                          """,(yil))
            liste = list()
            for item in data:
                model = MkRaporlarSevkSipModel()
                yuklenen = self.__getYuklenenSiparisler(item.SiparisNo)
                if(self.__getYuklenenSiparisler(item.SiparisNo) == None):
                    model.po = item.SiparisNo
                    model.siparisfob = self.__noneControl(item.SatisToplam)
                    model.yuklenenfob = self.__noneControl(0)
                    model.yuklemetarihi = ""
                    model.yuklenenddp = model.yuklenenfob + self.__noneControl(self.__getYuklenenMasrafPo(item.SiparisNo))
                    model.musteriadi = item.FirmaAdi
                    model.teslimtur = item.TeslimTur
                    model.siparistarihi = item.SiparisTarihi
                else:
                    model.po = item.SiparisNo
                    model.siparisfob = self.__noneControl(item.SatisToplam)
                    model.yuklenenfob = self.__noneControl(yuklenen.SatisToplam)
                    model.yuklemetarihi = yuklenen.YuklemeTarihi
                    model.yuklenenddp = model.yuklenenfob + self.__noneControl(self.__getYuklenenMasrafPo(item.SiparisNo))
                    model.musteriadi = item.FirmaAdi
                    model.teslimtur = item.TeslimTur
                    model.siparistarihi = item.SiparisTarihi
                    
                
                liste.append(model)
            schema = MkRaporlarSevkSipSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('mkRaporlarSevkSip hata',str(e))
            return False
    
    
    def __getYuklenenSiparisler(self,po):
        for item in self.yuklenenPo:
            if(item.SiparisNo == po):
                return item
    
    def __getYuklenenMasrafPo(self,po):
        for item in self.yuklenenPoMasraf:
            if(item.SiparisNo == po):
                return item.Masraflar
    
    def __getYuklenenMasraf(self,firma):
        for item in self.yuklenenMusteriMasraf:
            if(item.FirmaAdi == firma):
                return item.NavlunvDiger
            
    def __noneControl(self,value):
        if(value == None):
            return 0
        else:
            return float(value)
            