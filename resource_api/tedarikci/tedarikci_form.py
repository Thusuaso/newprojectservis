from helpers import SqlConnect,TarihIslemler
from  models.tedarikci_form import TedarikciFormSchema,TedarikciFormModel




class TedarikciFormIslem:

    def __init__(self):

        self.data = SqlConnect().data

    def getTeslimTurListe(self):
        
        result = self.data.getList(
            """
            select * from Tedarikci_Teslim_TurTB
            """
        )

        liste = list()

        for item in result:

            model = {

                "id" : item.ID,
                "teslim_adi" : item.TeslimAdi
            }

            liste.append(model)

        return liste
    
    def getFaturaTurList(self):
        
        result = self.data.getList(

            """
            select * from TedarikciSiparisFaturaTurTB
            """

        )
        
        liste = list()

        for item in result:

            model = {

                "id" : item.ID,
                "fatura_tur" : item.FaturaTanim
            }

            liste.append(model)

        return liste

    def tedarikciFormKontrol(self,siparis_no,tedarikci_id):

        kontrol = self.data.getStoreList(
            """
            select count(*) durum from SiparisUrunTedarikciFormTB 
            where SiparisNo=? and TedarikciID=?
            """,(siparis_no,tedarikci_id)
        )[0].durum

        return kontrol


    def getTedarikciFormModel(self):
        
        model = TedarikciFormModel()

        schema = TedarikciFormSchema()

        return schema.dump(model)

    def getTedarikciForm(self,id):
        
        tarihIslem = TarihIslemler()
        item = self.data.getStoreList(

            """
            select * from 
            SiparisUrunTedarikciFormTB where ID=?
            """,(id)
        )[0]

        model = TedarikciFormModel()
        model.id = item.ID
        model.siparis_no = item.SiparisNo
        model.fatura_tur_id = item.TedarikciSiparisFaturaTurID
        model.teslim_id = item.TedarikciTeslimTurID

        if item.SiparisTarihi != None:
            model.siparis_tarihi = tarihIslem.getDate(item.SiparisTarihi).strftime("%d-%m-%Y")

        if item.TeslimTarihi != None:
            model.siparis_tarihi = tarihIslem.getDate(item.TeslimTarihi).strftime("%d-%m-%Y")

        model.madde4 = item.Madde4
        model.madde5 = item.Madde5
        
        schema = TedarikciFormSchema()

        return schema.dump(model)
        

    def kaydet(self,item):
        try:
            kullanici_id = self.data.getStoreList(
                """
                select ID from KullaniciTB 
                where KullaniciAdi=?
                """,(item['kullanici_adi'])

            )
            print("UrunTedarikciKayıt",item)
            self.data.update_insert(
                """
                insert into SiparisUrunTedarikciFormTB (
                    SiparisNo,TedarikciID,TedarikciSiparisFaturaTurID,
                    TedarikciTeslimTurID,SiparisTarihi,TeslimTarihi,
                    Madde4,Madde5,KullaniciID
                )
                values
                (
                    ?,?,?,?,?,?,?,?,?
                )
                """,(

                    item['siparis_no'],item['tedarikci_id'],item['fatura_tur_id'],
                    item['teslim_id'],item['siparis_tarihi'],item['teslim_tarihi'],
                    item['madde4'],item['madde5'],kullanici_id
                )
               
            )
            return True
        except Exception as e:
            print('TedarikciFormIslem kaydet Hata : ',str(e))
            return False

    def guncelle(self,item):

        try:
            kullanici_id = self.data.getStoreList(
                """
                select ID from KullaniciTB 
                where KullaniciAdi=?
                """,(item['kullanici_adi'])

            )

            self.data.update_insert(

                """
                update SiparisUrunTedarikciFormTB set 
                TedarikciID=?,TedarikciSiparisFaturaTurID=?,
                TedarikciTeslimTurID=?,SiparisTarihi=?,
                TeslimTarihi=?,Madde4=?,Madde5=?,
                KullaniciID=? where ID=?
                """,(

                    item['tedarikci_id'],item['fatura_tur_id'],
                    item['teslim_id'],item['siparis_tarihi'],
                    item['teslim_tarihi'],item['madde4'],
                    item['madde5'],kullanici_id,item['id']
                )
            )

            return True

        except Exception as e:
            print('TedarikciFormIslem güncelle hata: ',str(e))
            return False
    