from openpyxl import *
from openpyxl.styles import Border, Side , Font ,Alignment,PatternFill
from openpyxl.cell import Cell
import shutil



class ExcelCiktiIslemMusteri:

    def musteri_rapor_ciktisi(self,data_list):
        
        try:
            source_path = 'resource_api/raporlar/sablonlar/musteri_listesi.xlsx'
            target_path = 'resource_api/raporlar/dosyalar/musteri_listesi.xlsx'

            shutil.copy2(source_path, target_path)
            

            kitap = load_workbook(target_path)
            sayfa = kitap.get_sheet_by_name('Sayfa1')

            satir = 2

            for item in data_list:
                sayfa.cell(satir,column=1,value=item['musteri'])
                sayfa.cell(satir,column=2,value=item['ulkeAdi'])
                sayfa.cell(satir,column=3,value=item['temsilci'])
                
                if item['Toplam'] == None:
                    sayfa.cell(satir,column=4,value=0)
                else:
                    sayfa.cell(satir,column=4,value=item['Toplam'])
                
                
                
                if item['BuYilUretim'] == None:
                    sayfa.cell(satir,column=5,value=0) 
                else:
                    sayfa.cell(satir,column=5,value=item['BuYilUretim']) 

                if item['BuYilSevkiyat'] == None:
                    sayfa.cell(satir,column=6,value=0) 
                else:
                    sayfa.cell(satir,column=6,value=item['BuYilSevkiyat']) 
                
                

                if item['GecenYil'] == None:
                    sayfa.cell(satir,column=7,value=0) 
                else:
                    sayfa.cell(satir,column=7,value=item['GecenYil']) 

                if item['OncekiYil'] == None:
                    sayfa.cell(satir,column=8,value=0) 
                else:
                    sayfa.cell(satir,column=8,value=item['OncekiYil'])
                    
                if item['OnDokuzYili'] == None:
                    sayfa.cell(satir,column=9,value=0) 
                else:
                    sayfa.cell(satir,column=9,value=item['OnDokuzYili']) 
                    
                if item['OnSekizYili'] == None:
                    sayfa.cell(satir,column=10,value=0) 
                else:
                    sayfa.cell(satir,column=10,value=item['OnSekizYili'])                 
                
                if item['OnYediYili'] == None:
                    sayfa.cell(satir,column=11,value=0) 
                else:
                    sayfa.cell(satir,column=11,value=item['OnYediYili']) 
                
                if item['OnAltiYili'] == None:
                    sayfa.cell(satir,column=12,value=0) 
                else:
                    sayfa.cell(satir,column=12,value=item['OnAltiYili']) 
                    
                if item['OnBesYili'] == None:
                    sayfa.cell(satir,column=13,value=0) 
                else:
                    sayfa.cell(satir,column=13,value=item['OnBesYili']) 
                
                
                if item['OnDortYili'] == None:
                    sayfa.cell(satir,column=14,value=0) 
                else:
                    sayfa.cell(satir,column=14,value=item['OnDortYili']) 
                
                if item['OnUcYili'] == None:
                    sayfa.cell(satir,column=15,value=0) 
                else:
                    sayfa.cell(satir,column=15,value=item['OnUcYili']) 
                
                if item['OnUcYiliOncesi'] == None:
                    sayfa.cell(satir,column=16,value=0) 
                else:
                    sayfa.cell(satir,column=16,value=item['OnUcYiliOncesi']) 
                
                
                
             

                satir += 1
            
            kitap.save(target_path)
            kitap.close()
            

            return True

        except Exception as e:
            print('MusteriBazındaListe ExcellÇıktı Hata : ',str(e))
            return False
    def musteri_sip_rapor_ciktisi(self,data_list):
        
        
        try:
            source_path = 'resource_api/raporlar/sablonlar/musteriSipYilListesi.xlsx'
            target_path = 'resource_api/raporlar/dosyalar/musteriSipYilListesi.xlsx'

            shutil.copy2(source_path, target_path)
            

            kitap = load_workbook(target_path)
            sayfa = kitap.get_sheet_by_name('Sayfa1')

            satir = 2

            for item in data_list:
                sayfa.cell(satir,column=1,value=item['ay'])
                sayfa.cell(satir,column=2,value=item['fob'])
                sayfa.cell(satir,column=3,value=item['ddp'])
                sayfa.cell(satir,column=4,value=item['fark'])
                
                
                
                
             

                satir += 1
            
            kitap.save(target_path)
            kitap.close()
            

            return True

        except Exception as e:
            
            print('MusteriSipYilBazındaListe ExcellÇıktı Hata : ',str(e))
            return False
        
        
        
    def musteri_sip_buYil_ayrinti_rapor_ciktisi(self,data_list):
        
        try:
            source_path = 'resource_api/raporlar/sablonlar/musteriSipBuYilAyrintiListesi.xlsx'
            target_path = 'resource_api/raporlar/dosyalar/musteriSipBuYilAyrintiListesi.xlsx'

            shutil.copy2(source_path, target_path)
            

            kitap = load_workbook(target_path)
            sayfa = kitap.get_sheet_by_name('Sayfa1')

            satir = 2

            for item in data_list:
                sayfa.cell(satir,column=1,value=item['musteri'])
                sayfa.cell(satir,column=2,value=item['fob'])
                sayfa.cell(satir,column=3,value=item['navlun'])
                sayfa.cell(satir,column=4,value=item['detay1'])
                sayfa.cell(satir,column=5,value=item['detay2'])
                sayfa.cell(satir,column=6,value=item['detay3'])
                sayfa.cell(satir,column=7,value=item['detay4'])
                sayfa.cell(satir,column=8,value=item['ddp'])
             

                satir += 1
            
            kitap.save(target_path)
            kitap.close()
            

            return True

        except Exception as e:
            
            print('MusteriSipYilBazındaListe ExcellÇıktı Hata : ',str(e))
            return False
        
    def musteri_sip_gecenYil_ayrinti_rapor_ciktisi(self,data_list):
        
        
        
        try:
            source_path = 'resource_api/raporlar/sablonlar/musteriSipGecenYilAyrintiListesi.xlsx'
            target_path = 'resource_api/raporlar/dosyalar/musteriSipGecenYilAyrintiListesi.xlsx'

            shutil.copy2(source_path, target_path)
            

            kitap = load_workbook(target_path)
            sayfa = kitap.get_sheet_by_name('Sayfa1')

            satir = 2

            for item in data_list:
                sayfa.cell(satir,column=1,value=item['musteri'])
                sayfa.cell(satir,column=2,value=item['fob'])
                sayfa.cell(satir,column=3,value=item['navlun'])
                sayfa.cell(satir,column=4,value=item['detay1'])
                sayfa.cell(satir,column=5,value=item['detay2'])
                sayfa.cell(satir,column=6,value=item['detay3'])
                sayfa.cell(satir,column=7,value=item['detay4'])
                sayfa.cell(satir,column=8,value=item['ddp'])
             

                satir += 1
            
            kitap.save(target_path)
            kitap.close()
            

            return True

        except Exception as e:
            
            print('MusteriSipGecenYilBazındaListe ExcellÇıktı Hata : ',str(e))
            return False
        
    def musteri_sip_oncekiYil_ayrinti_rapor_ciktisi(self,data_list):
        
        
        
        try:
            source_path = 'resource_api/raporlar/sablonlar/musteriSipOncekiYilAyrintiListesi.xlsx'
            target_path = 'resource_api/raporlar/dosyalar/musteriSipOncekiYilAyrintiListesi.xlsx'

            shutil.copy2(source_path, target_path)
            

            kitap = load_workbook(target_path)
            sayfa = kitap.get_sheet_by_name('Sayfa1')

            satir = 2

            for item in data_list:
                sayfa.cell(satir,column=1,value=item['musteri'])
                sayfa.cell(satir,column=2,value=item['fob'])
                sayfa.cell(satir,column=3,value=item['navlun'])
                sayfa.cell(satir,column=4,value=item['detay1'])
                sayfa.cell(satir,column=5,value=item['detay2'])
                sayfa.cell(satir,column=6,value=item['detay3'])
                sayfa.cell(satir,column=7,value=item['detay4'])
                sayfa.cell(satir,column=8,value=item['ddp'])
             

                satir += 1
            
            kitap.save(target_path)
            kitap.close()
            

            return True

        except Exception as e:
            
            print('MusteriSipOncekiYilBazındaListe ExcellÇıktı Hata : ',str(e))
            return False
        
        
        
    def get_ulke_bazinda_sip_top(self,data_list):
        
        
        try:
            source_path = 'resource_api/raporlar/sablonlar/ulkebzindaSevkiyat.xlsx'
            target_path = 'resource_api/raporlar/dosyalar/ulkebzindaSevkiyat.xlsx'

            shutil.copy2(source_path, target_path)
            

            kitap = load_workbook(target_path)
            sayfa = kitap.get_sheet_by_name('Sayfa1')

            satir = 2

            for item in data_list:
                sayfa.cell(satir,column=1,value=item['ulkeadi'])
                sayfa.cell(satir,column=2,value=item['toplamsevkiyat'])
 
                
                
                
                
             

                satir += 1
            
            kitap.save(target_path)
            kitap.close()
            

            return True

        except Exception as e:
            
            print('Ulke Bazinda Sevkiyat ExcellÇıktı Hata : ',str(e))
            return False
        