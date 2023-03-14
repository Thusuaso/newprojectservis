from helpers import SqlConnect,TarihIslemler,MailService,DegisiklikMain
from models.finans import TahsilatModel,TahsilatSchema
import datetime
from views.raporlar import AnaSayfaDegisiklik

class TahsilatIslem:

    def __init__(self): 

        self.data = SqlConnect().data
        self.musteriadi = ""


    def getTahsilatList(self,musteriid,siparisNo):

        tarihIslem = TarihIslemler()
        result = self.data.getStoreList(

            """
            Select
            o.ID,
            o.SiparisNo,
            o.Tarih,
            o.Tutar,
            o.Masraf,
            m.FirmaAdi,
            o.MusteriID,
            o.Aciklama, 
            o.Kur
            from OdemelerTB o,MusterilerTB m
            where
            m.ID = o.MusteriID and 
            o.SiparisNo=? and o.MusteriID=?
            """,(siparisNo,musteriid)
        )
        
        liste = list()
        self.musteriadi = self.data.getStoreList(
            """
            Select FirmaAdi from MusterilerTB
            where ID=?
            """,(musteriid)
        )[0].FirmaAdi

        for item in result:

            model = TahsilatModel()
            model.id = item.ID
            model.siparisno = item.SiparisNo
            model.tarih = tarihIslem.getDate(item.Tarih).strftime("%d-%m-%Y")
            model.tutar = item.Tutar
            model.masraf = item.Masraf
            model.kur = item.Kur
            model.musteriadi = item.FirmaAdi
            model.musteri_id = item.MusteriID
            model.aciklama = item.Aciklama

            liste.append(model)

        schema = TahsilatSchema(many=True)

        return schema.dump(liste)

    def getTahsilatModel(self,musteriid,siparisNo):

        model = TahsilatModel()
        model.siparisno = siparisNo
        model.musteri_id = musteriid
        model.musteriadi = self.musteriadi
       

        schema = TahsilatSchema()
        
        return schema.dump(model)

    def tahsilatKaydet(self,item):
        tarih = item['tarih']
        forMat = '%d-%m-%Y'
        tarih = datetime.datetime.strptime(tarih, forMat)
        tarih = tarih.date()
        try:
            kullaniciid = self.data.getStoreList(
                """
                Select ID from KullaniciTB
                where KullaniciAdi=?
                """,(item['kullaniciadi'])
            )[0].ID

            self.data.update_insert(
                """
                insert into OdemelerTB (
                    Tarih,MusteriID,SiparisNo,FinansOdemeTurID,
                    Aciklama,Tutar,Masraf,KullaniciID,Kur
                )
                values
                (?,?,?,?,?,?,?,?,?)
                """,
                (
                    tarih,item['musteri_id'],item['siparisno'],
                    1,item['aciklama'],item['tutar'],item['masraf'],kullaniciid,item['kur']
                )
            )
            self.mailGonder(item['siparisno'],'Yeni Tahsilat Girişi',item['tutar'],item['tarih'],item['masraf'],item['kullaniciadi'])
            info =item['kullaniciadi'].capitalize() + ', ' + item['siparisno'] + ' $' + str(item['tutar']) +' Tahsilat Girişi Yaptı'
            DegisiklikMain().setYapilanDegisiklikBilgisi(item['kullaniciadi'].capitalize(),info)
            islem = AnaSayfaDegisiklik()
            anaSayfaDegisiklikList = islem.getAnaSayfaDegisiklik()
            data = {
                'status':True,
                'anaSayfaDegisiklikList':anaSayfaDegisiklikList,
                'siparisno':item['siparisno']
            }
            return data
        except Exception as e:
            print('Tahsilat Kaydet Hata : ',str(e))
            return False

    def tahsilatGuncelle(self,item):
        tarih = item['tarih']
        forMat = '%d-%m-%Y'
        tarih = datetime.datetime.strptime(tarih, forMat)
        tarih = tarih.date()
        try:
            kullaniciid = self.data.getStoreList(
                """
                Select ID from KullaniciTB
                where KullaniciAdi=?
                """,(item['kullaniciadi'])
            )[0].ID

            self.data.update_insert(

                """
                update OdemelerTB set Tarih=?,Tutar=?,
                Masraf=?,Aciklama=?,KullaniciID=?,Kur =?
                where ID=?
                """,(
                    tarih,item['tutar'],item['masraf'],
                    item['aciklama'],kullaniciid,item['kur'],item['id']
                )
            )

            self.mailGonder(item['siparisno'],'Tahsilat Değiştirme',item['tutar'],item['tarih'],item['masraf'],item['kullaniciadi'])
            info =item['kullaniciadi'] + ' ' + item['siparisno'] + ' ' + 'ya Tahsilat Değişikliği Yaptı'
            DegisiklikMain().setYapilanDegisiklikBilgisi(item['kullaniciadi'],info)
            islem = AnaSayfaDegisiklik()
            anaSayfaDegisiklikList = islem.getAnaSayfaDegisiklik()
            data = {
                'status':True,
                'anaSayfaDegisiklikList':anaSayfaDegisiklikList,
                'siparisno':item['siparisno']
            }
            return data
        except Exception as e:
            print('Tahsilat Güncelleme Hata : ',str(e))
            return False

    def tahsilatSilme(self,id):
        try:
            result = self.data.getStoreList(

                """
                select * from OdemelerTB where ID=?
                """,(id)
            )
            self.data.update_insert(
                """
                delete from OdemelerTB where ID=?
                """,(id)
            )

            self.mailGonder(result.SiparisNo,'Tahsilat Silme İşlemi',result.Tutar,result.Tarih,result.Masraf,result.KullaniciID)
            if result.KullaniciID == 12:
                info ='Hüseyin' + ' ' + result.SiparisNo + ' ' + 'nın Tahsilatını Sildi.'
                DegisiklikMain().setYapilanDegisiklikBilgisi('Hüseyin',info)
            elif result.KullaniciID == 10:
                info ='Gizem' + ' ' + result.SiparisNo + ' ' + 'nın Tahsilatını Sildi.'
                DegisiklikMain().setYapilanDegisiklikBilgisi('Gizem',info)
            return True
        except Exception as e:
            print('Tahsilat Silme Hata : ',str(e))
            return False

    def mailGonder(self,siparis_no,islem_aciklamasi,tutar,tarih,masraf,kullanici):

        result = self.data.getStoreList(
            """
            select 
            k.MailAdres,
			m.FirmaAdi,
            m.Marketing
            from 
            SiparislerTB s,KullaniciTB k,MusterilerTB m
            where s.SiparisNo=?
            and k.ID=s.SiparisSahibi
			and m.ID=s.MusteriID
            """,(siparis_no)
        )[0]

        ilgili_mail_adres = result.MailAdres

        musteri_adi = result.FirmaAdi

        mail_konu = f""" 
            {musteri_adi}-{siparis_no}- {tarih} - ${tutar}  / ${masraf}  -

            {kullanici} tarafından işlendi . 
            """



        MailService(islem_aciklamasi,"huseyin@mekmarmarble.com",mail_konu)
        MailService(islem_aciklamasi,"mehmet@mekmer.com",mail_konu)
        
       
        MailService(islem_aciklamasi,ilgili_mail_adres,mail_konu)
        if result.Marketing == 'Mekmar' : 
               MailService(islem_aciklamasi,"info@mekmar.com",mail_konu)

    def setOdemeDegisim(self,data):
        newSipNo = data['siparisno']['siparisNo']
        newtutar = data['tutar']
        degisenOdemeId = data['odemeId']
        newAciklama = data['aciklama']
        kullanici = data['kullanici']
        degisenOdeme = self.data.getStoreList("""
                                                select * from OdemelerTB where ID=?
                                              


        
                                              """,(degisenOdemeId))
        
        
        
        
        info = kullanici + ' ' + degisenOdeme[0].SiparisNo + ' daki $ ' +str(degisenOdeme[0].Tutar) + ' tutarından $ ' + str(newtutar) + ' tutarını ' + newSipNo + ' ya aktarmıştır.'
        yukleme_tarihi = None
        DegisiklikMain().setMaliyetDegisiklik(info,kullanici,newSipNo,yukleme_tarihi) 
        
        
        for item in degisenOdeme:
            item.Tutar = float(item.Tutar) - float(newtutar)
            if item.Tutar < 0 or item.Tutar==0:
                self.__updateOdemeSipNo(item.ID,newSipNo)
            else:
                self.__updateOdeme(item.ID,item.Tutar)
                self.__insertOdemeNew(item,newSipNo,newtutar,newAciklama)
            
            
        
            
            
    def __updateOdeme(self,id,tutar):
        self.data.update_insert("""

                                    update OdemelerTB SET Tutar=? WHERE ID=?
                                
                                """,(tutar,id))
    def __insertOdemeNew(self,item,newSipNo,newtutar,newAciklama):
        self.data.update_insert("""
                                    insert into 
                                    OdemelerTB(Tarih,MusteriID,SiparisNo,FinansOdemeTurID,Aciklama,Tutar,Masraf,KullaniciID,Kur) 
                                    VALUES(?,?,?,?,?,?,?,?,?)
                                
                                """,(item.Tarih,item.MusteriID,newSipNo,item.FinansOdemeTurID,newAciklama,newtutar,0,item.KullaniciID,item.Kur))
        
    def __updateOdemeSipNo(self,id,siparisno):
        self.data.update_insert("""

                                    update OdemelerTB SET SiparisNo=? WHERE ID=?
                                
                                """,(siparisno,id))
            
        





