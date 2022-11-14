import boto3
from boto3 import session
from botocore.client import Config
from boto3.s3.transfer import S3Transfer
import os


class BulutIslem:
    def __init__(self):

        session = boto3.session.Session()

        self.client = session.client(
            's3',
            region_name='fra1',
            endpoint_url='https://fra1.digitaloceanspaces.com',
            aws_access_key_id = 'B7POIPPYM44Y374P23KS',
            aws_secret_access_key='01CMWBcNKtFgKG6XhP+q0PlajTb2yvELaJ1igo7xsyA'
        )

    def dosyaKayit(self,file):

        path = 'public/'
        self.filePath = path + file.filename
        self.filename = file.filename
        #foto data kayıt işlemleri
        file.save(os.path.join(path,file.filename))
        self.__dosyaGonder()
        return True

    def __dosyaGonder(self):
        self.client.upload_file(

            self.filePath,
            'mekmar-image',
            'products/' + self.filename,
            ExtraArgs={ "ContentType": "image/" + str(self.filename).split('.')[1], 'ACL' : 'public-read' }
        )

        os.remove(self.filePath)

    def dosyaGonderPdf(self,space_path,file):
        try:
            path = 'public/'
            filename = file.filename 
            filepath = path + filename
            file.save(os.path.join(path,filename))

            self.client.upload_file(
                filepath,
                'mekmar-image',
                str(space_path) + filename,
                ExtraArgs={ "ContentType" : "application/pdf",'ACL' : 'public-read' }
            )
            return True
        except Exception as e:
            print('dosyaGonderPdf Hata : ',str(e))
            return False
