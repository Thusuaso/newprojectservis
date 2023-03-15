import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys
class MailService:

    def __init__(self,subject,to,body):

        self.subject = subject
        self.to = to 
        self.body = body
        self.mailGonder()

    def mailGonder(self):
        try:
            mail = smtplib.SMTP("mail.mekmar.com",587)
            mail.ehlo()
            mail.starttls()
            mail.login("gozmek@mekmar.com", "w_FrBO87:3K3nz==")

            mesaj = MIMEMultipart()
            mesaj["From"] = "gozmek@mekmar.com"           # Gönderen
            mesaj["Subject"] = self.subject

            mesaj["To"] = self.to
            body_text = MIMEText(self.body, "html")  #
            mesaj.attach(body_text)
            
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            mail.close()
        except:
            print("Hata:", sys.exc_info()[0])
            

