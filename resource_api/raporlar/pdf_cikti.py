from reportlab.pdfgen import canvas
from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak, Image, Spacer, Table, TableStyle)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import LETTER, inch
from reportlab.graphics.shapes import Line, LineShape, Drawing
from reportlab.lib.colors import Color
from reportlab.pdfbase.ttfonts  import TTFont
from reportlab.pdfbase          import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

from helpers import SqlConnect,TarihIslemler

import datetime
from datetime import date
class FooterCanvas():

   def pdfciktisi(self,data_list):
         
    
      
        
        
        pdf = canvas.Canvas("Form.pdf",pagesize=A4)
      
        pdfmetrics.registerFont(
            TTFont('TurkishRegular', r'comfortaa-cufonfonts\Comfortaa_Regular.ttf')
        )
       
        pdf.setFont("TurkishRegular", 8)
        idx = 5
        row = 5
        i = 0 
        j= 1
        
        
        
      
        
        matrix = [

        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
        ['','','','','','',''],
         ['','','','','','',''],
        ['','','','','','',''],
      

       ]
      
        matrix[0][0]  = 'Ürün Adı '
        matrix[0][1]  = 'Yüzey İşlemi'  
        matrix[0][2]  = 'Ölçü(cm) '
        matrix[0][3]  = 'Miktar' 
        matrix[0][4]  = 'Birim' 
        matrix[0][5]  = 'Birim Fiyat' 
        matrix[0][6]  = 'Toplam' 
        
      
        idx = 5
        i = 1
        bedel = 0
        for ridx, row in enumerate(matrix):
            for cidx, col in enumerate(row):
                matrix[i][0] = data_list[idx]['urunAdi']
                matrix[i][1] = data_list[idx]['uretimAciklama']
                matrix[i][2] = data_list[idx]['en'] + 'x'+  data_list[idx]['boy']+ 'x'+  data_list[idx]['kenar']
                matrix[i][3] = data_list[idx]['miktar']
                matrix[i][4] = data_list[idx]['urunbirimAdi']
                matrix[i][5] = "${:,.2f}".format(data_list[idx]['alisFiyati']) 
                matrix[i][6] =  "${:,.2f}".format(data_list[idx]['alisFiyati']*data_list[idx]['miktar'] )  
                bedel = bedel +  data_list[idx]['alisFiyati']*data_list[idx]['miktar']
                idx +=1
               
                
                
               

                i+= 1

                if idx == len(data_list):
                    break
            if  idx == len(data_list):
                break        

        myTable = Table(matrix)
        
       # Step 2) Set the new font, 
        # in this case I'm adding just for the second row of the table
        uzunluk = len(data_list)-5
        myTable.setStyle([
          ('FONTNAME', (0, 0),  (-1,-1), 'TurkishRegular'),

          ('GRID', (0,0), (-1,uzunluk), 1, 'black'),
          ('FONTSIZE',(0,0),(-1,-1),7)
      ])
          
       
        tarihIslem = TarihIslemler()
        bugun = tarihIslem.getDate( date.today()).strftime("%d-%m-%Y")   

        pdfmetrics.registerFont(TTFont('Hebrew', 'Arial.ttf'))
        pdf.setFont("Hebrew", 8)
        pdf.drawImage("https://mekmar-image.fra1.digitaloceanspaces.com/logo/baslik.png", 10, 710, width=580, height=130) 

        pdf.drawString(50,690, 'Kasa Uzerine : ')
        pdf.drawString(150,690, data_list[5]['siparisNo'])

        pdf.drawString(50,680, 'Siparis Tarihi: ')
        pdf.drawString(150,680,bugun)

        pdf.drawString(50,670, 'Firma: ')
        pdf.drawString(150,670, data_list[5]['tedarikciAdi'])

        pdf.drawString(50,660, 'Teslimat : ')
        pdf.drawString(150,660, data_list[0]['teslimAdi'])

        pdf.drawString(50,650, 'Teslim : ')
        pdf.drawString(150,650, data_list[1])
        pdf.setFont('Helvetica-Bold', 10)
        pdf.drawString(430,300, "Total  : " )
        pdf.drawString(460,300, "${:,.2f}".format(bedel ) )

        

        pdf.setFont("Hebrew", 8)
        pdf.drawString(10,200, u"Sayın İlgili ; Siparişi Onaylayınız ve Teslim Tarihi Bildiriniz. " .encode('utf-8'))
        pdf.drawString(10,180, u"Şartlar : " .encode('utf-8'))
        pdf.drawString(10,170, u"1.Malzeme aynen yukarda belirtildiği gibi tüm detaylara uygun olarak hazırlanmalıdır ." .encode("utf-8"))
        pdf.drawString(10,160, u"2.Kasalar ısıl işlemli ve bağlı olacak." .encode('utf-8'))
        pdf.drawString(10,150, u"3." .encode("utf-8"))
        pdf.drawString(20,150, data_list[3])
        pdf.drawString(10,140, u"4." .encode("utf-8"))
        pdf.drawString(20,140, data_list[4])
        pdf.drawString(10,130, u"5.Belirtilen şartlara uymayan malzemelerin tüm sorumluluğu üreticiye aittir." .encode("utf-8"))
        pdf.drawString(10,100, u" Sipariş Formu sadece yukarıda belirtilen şahış ya da firma adına düzenlenmiştir ve onun tarafından kullanılabilir. " .encode("utf-8"))
        pdf.drawString(10,90, u" Herhangi bir sorunuz olması durumunda yukarıda verilen numaralardan bize ulaşabilirsiniz . " .encode("utf-8") )
        
        myTable.wrapOn(pdf, 10, 10)
        myTable.drawOn(pdf, 5, 350)
        pdf.save()
       
        
        return True
      

