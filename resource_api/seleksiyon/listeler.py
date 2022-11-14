from helpers import SqlConnect
from models.shared import CardListSchema,CardListModel 
from models.seleksiyon import SiparisAyrintiSchema,SiparisAyrintiModel
from models.seleksiyon import UretimOzetSchema,UretimOzetModel
from models.seleksiyon import UretimSipModel,UretimSipSchema
import datetime


class SeleksiyonListeler:
    def __init__(self):
        self.data = SqlConnect().data
        self.uretim_miktar_list = self.data.getList(
            """
            select
            UrunKartID,
            SiparisAciklama,
            TedarikciID,
            Sum(Miktar) as Miktar
            from
            UretimTB
            where UrunDurumID=1
            group by UrunKartID,SiparisAciklama,TedarikciID
            """
        )

    
    def getUretimSiparisListe(self):

        result =  self.data.getList(
            """
            select
            ID,
            SiparisNo
            from
            SiparislerTB
            where
            SiparisDurumID=2
            order by SiparisTarihi desc
            """
        )

        liste = list()

        for item in result:

            model = CardListModel()
            model.id = item.ID 
            model.name  = item.SiparisNo 

            liste.append(model)

        schema = CardListSchema(many=True)

        return schema.dump(liste)

    def getUretimSiparisDetayList(self):

        result = self.data.getList(
            """
            select
            u.ID,
            u.UrunKartID,
            u.SiraNo,
            u.UrunBirimID,
            (Select t.FirmaAdi from TedarikciTB t where t.ID=u.TedarikciID) as tedarikci,
            (select k.KategoriAdi from KategoriTB k where uk.KategoriID=k.ID ) as kategori,
            (select ut.UrunAdi from UrunlerTB ut where ut.ID=uk.UrunID ) as urunadi,
            (select y.YuzeyIslemAdi from YuzeyKenarTB y where y.ID=uk.YuzeyID) as kenarislem,
            dbo.Get_Ebat(uk.ID) as ebat,
            u.SiparisNo,
            u.TedarikciID,
            u.Miktar
            from
            SiparisUrunTB u,UrunKartTB uk
            where 
            uk.ID=u.UrunKartID and u.SiparisNo in
            (select s.SiparisNo from SiparislerTB s where s.SiparisNo=u.SiparisNo and s.SiparisDurumID=2)
            order by u.SiraNo asc
            

            """
        )

        liste = list()
        for item in result:

            model = SiparisAyrintiModel()

            model.id = item.ID 
            model.urunkart_id = item.UrunKartID 
            model.tanim = f"{item.SiraNo} - {item.tedarikci}/{item.kategori}/{item.urunadi}/{item.kenarislem}/{item.ebat}"
            model.siparisno = item.SiparisNo
            model.tedarikci = item.tedarikci 
            model.urunbirimid = item.UrunBirimID 
            
            if self.__getUretimMiktar(item.UrunKartID,item.TedarikciID,model.siparisno) <= item.Miktar:
                liste.append(model)

        schema = SiparisAyrintiSchema(many=True)

        return schema.dump(liste)

    def getUretimSiparisDetay(self,siparisno):

        result = self.data.getStoreList(
            """
            select
            u.ID,
            u.UrunKartID,
            u.SiraNo,
            u.UrunBirimID,
            (Select t.FirmaAdi from TedarikciTB t where t.ID=u.TedarikciID) as tedarikci,
            (select k.KategoriAdi from KategoriTB k where uk.KategoriID=k.ID ) as kategori,
            (select ut.UrunAdi from UrunlerTB ut where ut.ID=uk.UrunID) as urunadi,
            (select y.YuzeyIslemAdi from YuzeyKenarTB y where y.ID=uk.YuzeyID) as kenarislem,
            dbo.Get_Ebat(uk.ID) as ebat,
            u.SiparisNo,
            u.TedarikciID,
            u.Miktar
            from
            SiparisUrunTB u,UrunKartTB uk
            where 
            uk.ID=u.UrunKartID and u.SiparisNo in
            (select s.SiparisNo from SiparislerTB s where s.SiparisNo=u.SiparisNo and s.SiparisDurumID=2)
            and u.SiparisNo=? 
            order by u.SiraNo asc
            """,(siparisno)
        )

        liste = list()
     
        for item in result:
            model = SiparisAyrintiModel()

            model.id = item.ID 
            model.urunkart_id = item.UrunKartID 
            model.tanim = f"{item.SiraNo} - {item.tedarikci}/{item.kategori}/{item.urunadi}/{item.kenarislem}/{item.ebat}"
            model.siparisno = item.SiparisNo
            model.tedarikci = item.tedarikci 
            model.urunbirimid = item.UrunBirimID 

            uretim_miktar = self.__getUretimMiktar(model.urunkart_id,item.TedarikciID,model.siparisno)
            
            if uretim_miktar < item.Miktar :
                liste.append(model)

        schema = SiparisAyrintiSchema(many=True)

        return schema.dump(liste)


    def getUretimSiparisDetay_UrunKart(self,siparisno,urunkartid):

        result = self.data.getStoreList(
            """
            select
            u.ID,
            u.UrunKartID,
            u.SiraNo,
            u.UrunBirimID,
            (Select t.FirmaAdi from TedarikciTB t where t.ID=u.TedarikciID) as tedarikci,
            (select k.KategoriAdi from KategoriTB k where uk.KategoriID=k.ID ) as kategori,
            (select ut.UrunAdi from UrunlerTB ut where ut.ID=uk.UrunID) as urunadi,
            (select y.YuzeyIslemAdi from YuzeyKenarTB y where y.ID=uk.YuzeyID) as kenarislem,
            dbo.Get_Ebat(uk.ID) as ebat,
            u.SiparisNo,
            u.TedarikciID,
            u.Miktar
            from
            SiparisUrunTB u,UrunKartTB uk
            where 
            uk.ID=u.UrunKartID and u.SiparisNo in
            (select s.SiparisNo from SiparislerTB s where s.SiparisNo=u.SiparisNo and s.SiparisDurumID=2)
            and u.SiparisNo=? and u.UrunKartID=?
            order by u.SiraNo asc
            """,(siparisno,urunkartid)
        )

        liste = list()

        for item in result:
            model = SiparisAyrintiModel() 

            model.id = item.ID 
            model.urunkart_id = item.UrunKartID 
            model.tanim = f"{item.SiraNo} - {item.tedarikci}/{item.kategori}/{item.urunadi}/{item.kenarislem}/{item.ebat}"
            model.siparisno = item.SiparisNo
            model.tedarikci = item.tedarikci 
            model.urunbirimid = item.UrunBirimID 

            liste.append(model)

        schema = SiparisAyrintiSchema(many=True)

        return schema.dump(liste)

    def __getUretimMiktar(self,urunkartid,tedarikciid,siparisaciklama):

        uretim_miktar = 0

        for item in self.uretim_miktar_list:

            if item.UrunKartID == urunkartid and item.TedarikciID == tedarikciid and item.SiparisAciklama == siparisaciklama:
                uretim_miktar += item.Miktar 

        
        return uretim_miktar

    def getOcakList(self):

        result = self.data.getList(
            """
            select
            OcakAdi,
            ID
            from
            UrunOcakTB
            where OcakAdi!='' and OcakAdi is not null
            group by OcakAdi,ID

            """
        )

        liste = list()

        for item in result:

            model = CardListModel()
            model.id = item.ID 
            model.name = item.OcakAdi 

            liste.append(model)
            

        schema = CardListSchema(many=True)

        return schema.dump(liste)

    def getTedarikciList(self):

        result = self.data.getList(
            """
            select
            FirmaAdi,
            ID
            from
            TedarikciTB
            where FirmaAdi!=''
            and FirmaAdi is not null
            group by FirmaAdi,ID

            """
        )

        liste = list()
       

        for item in result:

            model = CardListModel()
            model.id = item.ID 
            model.name = item.FirmaAdi 

            liste.append(model)
            

        schema = CardListSchema(many=True) 
        
        return schema.dump(liste)

    def getUrunBirimList(self):

        result = self.data.getList(
            """
            select
            *
            from
            UrunBirimTB
            """
        )

        liste = list()

        for item in result:

            model = CardListModel()
            model.id = item.ID 
            model.name = item.BirimAdi 

            liste.append(model)

        
        schema = CardListSchema(many=True)

        return schema.dump(liste)

    def getUretimOzetList(self):

        gun = datetime.date.today()
        yil = gun.year 
        ay= gun .month 

        result = self.data.getStoreList("{call dbo.Get_Uretim_Ozet(?,?,?)}",(ay,yil,gun))

        liste = list()
        
        for item in result:

            model = UretimOzetModel()
            model.id = item.TedarikciID
            model.yil = float(item.Yil) 
            model.ay = float(item.Ay) 
           # model.gun = float(item.Gun) 

            if model.id == 1:
                model.tanim = 'Mekmer'
            if model.id == 123:
                model.tanim = 'Mek-Moz'
            if model.id == 99:
                model.tanim = 'Dış'

            liste.append(model)

        schema = UretimOzetSchema(many=True)
        
        return schema.dump(liste)

    def getUretimSiparisKalemDetay(self,siparisno,urunkartid):

        item = self.data.getStoreList(
            """
            select
            u.ID,
            u.UrunKartID,
            u.SiraNo,
            u.UrunBirimID,
            (Select t.FirmaAdi from TedarikciTB t where t.ID=u.TedarikciID) as tedarikci,
            (select k.KategoriAdi from KategoriTB k where uk.KategoriID=k.ID ) as kategori,
            (select ut.UrunAdi from UrunlerTB ut where ut.ID=uk.UrunID) as urunadi,
            (select y.YuzeyIslemAdi from YuzeyKenarTB y where y.ID=uk.YuzeyID) as kenarislem,
            dbo.Get_Ebat(uk.ID) as ebat,
            u.SiparisNo
            from
            SiparisUrunTB u,UrunKartTB uk
            where 
            uk.ID=u.UrunKartID and u.SiparisNo in
            (select s.SiparisNo from SiparislerTB s where s.SiparisNo=u.SiparisNo and s.SiparisDurumID=2)
			and u.SiparisNo=? and u.UrunKartID=?
            order by u.SiraNo asc
            """,(siparisno,urunkartid)
        )[0]

        

        model = SiparisAyrintiModel()

        model.id = item.ID 
        model.urunkart_id = item.UrunKartID 
        model.tanim = f"{item.SiraNo} - {item.tedarikci}/{item.kategori}/{item.urunadi}/{item.kenarislem}/{item.ebat}"
        model.siparisno = item.SiparisNo
        model.tedarikci = item.tedarikci 
        model.urunbirimid = item.UrunBirimID

        schema = SiparisAyrintiSchema()

        return schema.dump(model)

    
    def getUretimSipListesi(self):

        result = self.data.getList(
            """
            select SiparisNo as SNO from SiparislerTB where SiparisDurumID=2


            """
        )

        liste = list()

        for item in result:

            model = UretimSipModel()
            model.sipNo=item.SNO

            liste.append(model)
            

        schema = UretimSipSchema(many=True)

        return schema.dump(liste)

class UretimUrunKartKasaKontrol:
    def __init__(self):
        self.data = SqlConnect().data
        
    def getUretimUrunKartKasaKontrol(self,urunKartId):
        try:
            result = self.data.getStoreList("""
                                                select * from UretimTB where UrunKartID = ?
                                            """,urunKartId)
            if len(result) >0:
                return True
            else:
                return False
            
        except Exception as e:
            print("getUretimUrunKartKasaKontrol",str(e))
            return False