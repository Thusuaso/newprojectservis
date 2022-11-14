import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys



class MailAttempt:

    def __init__(self):
        pass

    def mailSend(self,musteriler,genelBakiye,to):
        try:
            mail = smtplib.SMTP("mail.mekmar.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("tracking@mekmar.com", "FHlq13I2")

            mesaj = MIMEMultipart()
            mesaj["From"] = "tracking@mekmar.com"           # Gönderen
            mesaj["Subject"] = "Finans Alacak Listesi"    # Konusu
            mesaj['To'] = to
            body =  """
                    <table >
                        <tr style ="background-color: #f2f2f2;">
                            <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 50px;">
                                Musteri Adı
                            </th>
                            <th style ="color: white;background-color: #4CAF50;text-align: left;  padding-bottom: 12px; padding-top: 12px; padding-top: 12px;padding: 8px; font-family: Arial, Helvetica, sans-serif; border-collapse: collapse;width: 100px;">
                                Risk Bakiyesi
                            </th>
                            
                        </tr>
                    """
            for m,g in zip(musteriler,genelBakiye):
                body += f"""
                    <tr style ="background-color: #ddd;">
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                        {m}
                        </td>
                        <td style ="border: 1px solid #ddd; padding: 8px;  font-family: Arial, Helvetica, sans-serif;border-collapse: collapse; width: 100px;">
                        {g}
                        </td>
                    </tr>

                """

            body = body + "</table>"
            body_text = MIMEText(body, "html")
            mesaj.attach(body_text)
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            print("Mail başarılı bir şekilde gönderildi.")
            mail.close()

        except:
            print("Hata:", sys.exc_info()[0])



