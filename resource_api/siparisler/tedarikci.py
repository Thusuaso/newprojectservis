from helpers import SqlConnect
from models.tedarikci_form import TedarikciFormSchema,TedarikciFormModel

class TedarikciSiparisIslemler:
    def __init__(self,siparisNo):
        self.data = SqlConnect().data
        self.siparisNo = siparisNo

    def getTedarikciListesi(self):
       
        result = self.data.getStoreList(
            """
            Select t.ID,t.FirmaAdi from TedarikciTB t,SiparisUrunTB u
            where u.TedarikciID=t.ID and u.SiparisNo=?
            group by t.ID,t.FirmaAdi
            """,(self.siparisNo)
        )

        liste = list()

        for item in result:

            model = {
                'id' : item.ID,
                'tedarikciAdi' : item.FirmaAdi
            }

            liste.append(model)

        return liste

    def getTedariciFaturaTurList(self):
        
        result = self.data.getList(
            """
            Select * from TedarikciSiparisFaturaTurTB
            """
        )

        liste = list()

        for item in result:

            model = {

                'id' : item.ID,
                'faturaTur' : item.FaturaTanim
            }

            liste.append(model)

        return liste

    def getTedarikciTeslimTurList(self):  #firma ? liman

        result = self.data.getList(
            """
            select * from Tedarikci_Teslim_TurTB
            """
        )

        liste = list()

        for item in result:

            model = {

                'id' : item.ID,
                'teslimAdi' : item.TeslimAdi
                }

            liste.append(model)

        return liste

