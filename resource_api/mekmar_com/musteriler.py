from models.mekmar_com import SiteMusteriSchema,SiteMusteriModel
from helpers import SqlConnect


class SiteMusteri:

    def __init__(self):

        self.data = SqlConnect().data

    
    def getMusteriListesi(self):

        result = self.data.getList(
            """
            select
            Id,
            adi,
            kullaniciadi,
            mailadres,
            telefon
            from
            MekmarCom_Musteriler
         

            """
        )

        liste = list()

        for item in result:

            model = SiteMusteriModel()
            model.id = item.Id 
            model.adi = item.adi 
            model.kullaniciadi = item.kullaniciadi
            model.mailadres = item.mailadres
            model.telefon = item.telefon

            liste.append(model)

        
        schema = SiteMusteriSchema(many=True)

        return schema.dump(liste)

    def musteriGuncelle(self,item):

        try:
            self.data.update_insert(
                """
                update MekmarCom_Musteriler set adi=?,
                kullaniciadi=?,mailadres=?,telefon=? where Id=?
                """,
                (
                    item['adi'],item['kullaniciadi'],item['mailadres'],
                    item['telefon'],item['id']
                )
            )

            return True 
        except Exception as e:
            print('Site Müşteri Güncelle Hata : ',str(e))
            return False

    def musteriKaydet(self,item):

        try:
            self.data.update_insert(
                """
                insert into MekmarCom_Musteriler (
                    adi,kullaniciadi,mailadres,
                    telefon
                )
                values
                (?,?,?,?)
                """,
                (
                    item['adi'],item['kullaniciadi'],
                    item['mailadres'],item['telefon']
                )
            )

            return True 
        except Exception as e:
            print('Site Müşteri Teklif Kaydet Hata : ',str(e))

            return False

    def getMusteri(self,id):

        item = self.data.getStoreList(
            """
            select
            Id,
            adi,
            kullaniciadi,
            mailadres,
            telefon
            from
            MekmarCom_Musteriler
            where Id=?
            """,
            (id)
        )[0]

        model = SiteMusteriModel()
        model.id = item.Id 
        model.adi = item.adi 
        model.kullaniciadi = item.kullaniciadi
        model.mailadres = item.mailadres
        model.telefon = item.telefon

        schema = SiteMusteriSchema()

        return schema.dump(model)

    def getYeniMusteri(self):

        model = SiteMusteriModel()
        schema = SiteMusteriSchema()

        return schema.dump(model)

    def musteriSil(self,id):

        try:
            self.data.update_insert(
                """
                delete from MekmarCom_Musteriler where Id=?
                """,
                (
                    id
                )
            )

            return True 

        except Exception as e:
             print('Site Müşteri Teklif Silme Hata : ',str(e))
             return False