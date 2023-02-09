from helpers.sqlConnect import SqlConnect
from models.mekmar_com.galleria import *
class Galleria():
    def __init__(self):
        self.data = SqlConnect().data
    
    def add(self,data):
        try:
            print(data)
            sira = 1
            for item in data:
                
                self.data.update_insert("""
                                        insert into MekmarCom_Galleria(Image_Jpg,Product_Id,FileName,Sira,Project_Id,Videos) VALUES(?,?,?,?,?,?)

                                    
                                    
                                    """,(item['link'],item['productId'],item['fileName'],sira,item['projectId'],0))
                sira += 1
            
            return True
        
        except Exception as e:
            print('Galleria add hata',str(e))
            return False
        
    def videos_add(self,data):
        try:
            self.data.update_insert("""
                                        insert into MekmarCom_Galleria(Image_Jpg,Product_Id,FileName,Sira,Project_Id,Videos) VALUES(?,?,?,?,?,?)
                                    """,(data['videos_link'],data['videos_product_id'],data['videos_file_name'],1,data['videos_project_id'],data['videos_control']))
            return True
        except Exception as e:
            print('videos_add hata',str(e))
            return False
        
    def getPhotos(self,product_id):
        try:
            result = self.data.getStoreList("""
                                                select 


                                                    mg.ID,
                                                    mg.Image_Jpg,
                                                    mg.Product_Id,
                                                    mg.FileName,
                                                    mg.Videos

                                                from MekmarCom_Galleria mg where mg.Product_Id=?
                                            
                                            """,(product_id))
            liste = list()
            for item in result:
                model = GalleriaPhotosModel()
                model.id = item.ID
                model.image_link = item.Image_Jpg
                model.product_id = item.Product_Id
                model.file_name = item.FileName
                model.videos_control = item.Videos
                liste.append(model)
                
            schema = GalleriaPhotosSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getPhotos hata',str(e))
            return False
        
    def deletePhotos(self,id):
        try:
            self.data.update_insert("""
                                        delete MekmarCom_Galleria where ID=?
                                    
                                    """,id)
            return True
        except Exception as e:
            print('deletePhotos hata',str(e))
            return False  