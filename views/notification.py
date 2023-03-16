from helpers import SqlConnect
from datetime import datetime

class Notification:
    def __init__(self):
        self.data = SqlConnect().data
        self.notificationSubList = self.data.getList("""
                                                        select 

                                                            ID,
                                                            Tarih,
                                                            NotificationId,
                                                            Queue,
                                                            Message,
                                                            Follow

                                                        from AnlikBildirimGeriDonusTB
                                                     
                                                     
                                                     """)
    def save(self,data):
        try:
            datetime.now()
            self.data.update_insert("""
                                    insert into 
                                    AnlikBildirimTB(
                                        Tarih,
                                        UserId,
                                        UserName,
                                        Message,
                                        Follow,
                                        WhoSendId,
                                        WhoSendName) 
                                    VALUES(?,?,?,?,?,?,?)
                                
                                """,(datetime.now(),
                                     data['userId'],
                                     data['userName'],
                                     data['message'],
                                     1,
                                     data['whoSendId'],
                                     data['whoSendName']
                                     )
                                )
            return True
        except Exception as e:
            print('Notification save hata',str(e))
            return False
    def update(self,data):
        pass
    def getList(self,id):
        try:
            result = self.data.getStoreList("""
                                                select 

                                                    ID,
                                                    Tarih,
                                                    UserId,
                                                    UserName,
                                                    Message,
                                                    Follow,
                                                    WhoSendId,
                                                    WhoSendName


                                                from AnlikBildirimTB
                                                where UserId =? or WhoSendId=?
                                                order by ID desc
                                            
                                            """,(id,id))
            liste = list()
            key = 0
            for item in result:
                liste.append({
                    'key':str(key),
                    'data':{
                        'id':item.ID,
                        'tarih':item.Tarih,
                        'user_id':item.UserId,
                        'user_name':item.UserName,
                        'message':item.Message,
                        'follow':item.Follow,
                        'who_send_id':item.WhoSendId,
                        'who_send_name':item.WhoSendName
                    },
                    'children':self.__getNotificationSubList(item.ID,key)
                })

                key += 1
            return liste
        except Exception as e:
            print('notification getList hata',str(e))  
            return False
    def __getNotificationSubList(self,notification_id,key):
        
        liste = list()
        key2 = 0
        for item in self.notificationSubList:
            if(item.NotificationId == notification_id):
                liste.append({
                    'key':str(key) + '-' + str(key2),
                    'data':{
                        'id':item.ID,
                        'notificationId':item.NotificationId,
                        'tarih':item.Tarih,
                        'message':item.Message
                    }
                })
                
                key2 += 1
                
