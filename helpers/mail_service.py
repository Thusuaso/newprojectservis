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

        mail = smtplib.SMTP("mail.mekmar.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("goz@mekmar.com", "MEkmar16260540")

        mesaj = MIMEMultipart()
        mesaj["From"] = "goz@mekmar.com"           # Gönderen
        mesaj["Subject"] = self.subject

        mesaj["To"] = self.to
        body_text = MIMEText(self.body, "html")  #
        mesaj.attach(body_text)
        
        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
        print("Mail başarılı bir şekilde gönderildi.")
        mail.close()
