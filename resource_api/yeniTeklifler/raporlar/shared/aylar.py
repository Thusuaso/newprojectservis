class Aylar:

    def __init__(self):

        liste = list()

        liste.append({'sira' : 1, 'ay' : 'Ocak'})
        liste.append({'sira' : 2, 'ay' : 'Şubat'}) 
        liste.append({'sira' : 3, 'ay' : 'Mart'})
        liste.append({'sira' : 4, 'ay' : 'Nisan'})
        liste.append({'sira' : 5, 'ay' : 'Mayıs'})
        liste.append({'sira' : 6, 'ay' : 'Haziran'})
        liste.append({'sira' : 7, 'ay' : 'Temmuz'})
        liste.append({'sira' : 8, 'ay' : 'Ağustos'})
        liste.append({'sira' : 9, 'ay' : 'Eylül'})
        liste.append({'sira' : 10, 'ay' : 'Ekim'})
        liste.append({'sira' : 11, 'ay' : 'Kasım'})
        liste.append({'sira' : 12, 'ay' : 'Aralık'})

        self.ayList = liste

    def getAyAdi(self,ay): 

        ayAdi = ''
        for item in self.ayList:

            if ay == item['sira']:
                ayAdi = item['ay']
        
        return ayAdi


        
