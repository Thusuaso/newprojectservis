from helpers import SqlConnect,TarihIslemler,MailService
from models.efesfinans import EfesTahsilatModel,EfesTahsilatSchema


class EfesTahsilatIslem:

    def __init__(self): 

        self.data = SqlConnect().data
        self.musteriadi = ""


    def getEfesTahsilatList(self,musteriid,siparisNo):

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
            o.Aciklama
            from OdemelerTB o,MusterilerTB m ,SiparislerTB s 
            where
            m.ID = o.MusteriID  and s.MusteriID=o.MusteriID  and s.SiparisNo = o.SiparisNo  and  s.FaturaKesimTurID=2
            and o.SiparisNo=? and o.MusteriID=?
           
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

            model = EfesTahsilatModel()
            model.id = item.ID
            model.siparisno = item.SiparisNo
            model.tarih = tarihIslem.getDate(item.Tarih).strftime("%d-%m-%Y")
            model.tutar = item.Tutar
            model.masraf = item.Masraf
            model.musteriadi = item.FirmaAdi
            model.musteri_id = item.MusteriID
            model.aciklama = item.Aciklama

            liste.append(model)

        schema = EfesTahsilatSchema(many=True)

        return schema.dump(liste)

    def getEfesTahsilatModel(self,musteriid,siparisNo):

        model = EfesTahsilatModel()
        model.siparisno = siparisNo
        model.musteri_id = musteriid
        model.musteriadi = self.musteriadi

        schema = EfesTahsilatSchema()

        return schema.dump(model)

    def efestahsilatKaydet(self,item):

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
                    Aciklama,Tutar,Masraf,KullaniciID
                )
                values
                (?,?,?,?,?,?,?,?)
                """,
                (
                    item['tarih'],item['musteri_id'],item['siparisno'],
                    1,item['aciklama'],item['tutar'],item['masraf'],kullaniciid
                )
            )
            self.mailGonder(item['siparisno'],'Yeni Tahsilat Girişi',item['tutar'],item['tarih'],item['masraf'])
            return True
        except Exception as e:
            print('Tahsilat Kaydet Hata : ',str(e))
            return False

    def efestahsilatGuncelle(self,item):

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
                Masraf=?,Aciklama=?,KullaniciID=?
                where ID=?
                """,(
                    item['tarih'],item['tutar'],item['masraf'],
                    item['aciklama'],kullaniciid,item['id']
                )
            )

            self.mailGonder(item['siparisno'],'Tahsilat Değiştirme',item['tutar'],item['tarih'],item['masraf'])

            return True
        except Exception as e:
            print('Tahsilat Güncelleme Hata : ',str(e))
            return False

    def efestahsilatSilme(self,id):
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

            self.mailGonder(result.SiparisNo,'Tahsilat Silme İşlemi',result.Tutar,result.Tarih,result.Masraf)
            
            return True
        except Exception as e:
            print('Tahsilat Silme Hata : ',str(e))
            return False

    def mailGonder(self,siparis_no,islem_aciklamasi,tutar,tarih,masraf):

        result = self.data.getStoreList(
            """
            select 
            k.MailAdres,
			m.FirmaAdi
            from 
            SiparislerTB s,KullaniciTB k,MusterilerTB m
            where s.SiparisNo=?
            and k.ID=s.SiparisSahibi
			and m.ID=s.MusteriID
            """,(siparis_no)
        )[0]

        ilgili_mail_adres = result.MailAdres

        musteri_adi = result.FirmaAdi

        mail_konu = f" {musteri_adi} {siparis_no} {tutar} {tarih} / {masraf} "

        MailService(islem_aciklamasi,"huseyin@mekmarmarble.com",mail_konu)
        MailService(islem_aciklamasi,"mehmet@mekmer.com",mail_konu)
        MailService(islem_aciklamasi,ilgili_mail_adres,mail_konu)








