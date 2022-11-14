from helpers import SqlConnect
from models.tedarikci_form import TedarikciFormSchema,TedarikciFormModel


class TedarikciIcSiparisListe:
    def __init__(self):
        self.data = SqlConnect().data
    
   

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

   