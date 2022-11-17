from helpers.sqlConnect import SqlConnect
import datetime
from models.teklifler.bgpProjectsModel import *
class BgpProjects():
    def __init__(self):
        self.data = SqlConnect().data
        
    def setBgpProjectsName(self,projectName,temsilci,bgpUlkeAdi,ulkeLogo):
        try:
            now = datetime.datetime.now()
            day = now.strftime("%d")
            month = now.strftime("%m")
            year = now.strftime("%Y")
            nowDate = year + '-' + month + '-' + day
            result = self.data.getStoreList("""
                                                select * from BgpNetworkProjects where ProjectName=?
                                            
                                            """,(projectName))
            
            if len(result) > 0:
                result = self.getBgpProjectList(temsilci)
                return False,result
            else:
                self.data.update_insert("""

                                            insert BgpNetworkProjects(ProjectName,DateofRegistiration,Temsilci,UlkeAdi,UlkeLogo) VALUES(?,?,?,?,?)
                                        
                                        """,(projectName,nowDate,temsilci,bgpUlkeAdi,ulkeLogo))
                result = self.getBgpProjectList(temsilci)
                return True,result
            
        except Exception as e:
            print('setBgpProjectsName',str(e))
            result = self.getBgpProjectList(temsilci)
            return False,result
    
    
    
    def setBgpProjectsNameChange(self,projectName,temsilci,bgpUlkeAdi,ulkeLogo,projectId):
        try:
            self.data.update_insert("""

                                        update BgpNetworkProjects set ProjectName=?,Temsilci=?,UlkeAdi=?,UlkeLogo=? where ID=?
                                    
                                    """,(projectName,temsilci,bgpUlkeAdi,ulkeLogo,projectId))

            result = self.getBgpProjectList(temsilci)
            return True,result
            
        except Exception as e:
            print('setBgpProjectsNameChange',str(e))
            result = self.getBgpProjectList(temsilci)
            return False,result
      
    
    
    def getBgpProjectList(self,temsilci):
        try:
            if temsilci == 19 or temsilci == 44:
                result = self.data.getStoreList("""
                                                    select * from BgpNetworkProjects where Temsilci=?
                                                
                                                """,(temsilci))
                liste = list()
                for item in result:
                    model = BgpProjectsListModel()
                    model.id = item.ID
                    model.projectName = item.ProjectName
                    model.dateOfRegistiration = item.DateofRegistiration
                    model.temsilci = item.Temsilci
                    if(item.Temsilci == 19):
                        model.borderColor = 'red'
                    elif item.Temsilci == 44:
                        model.borderColor = 'blue'
                    
                    model.ulkeAdi = item.UlkeAdi
                    model.ulkeLogo = item.UlkeLogo
                    model.filelink = item.Filelink
                    model.fileCloud = item.FileCloud
                    liste.append(model)
                schema = BgpProjectsListSchema(many=True)
                return schema.dump(liste)
            else:
                result = self.data.getList("""
                                                    select * from BgpNetworkProjects
                                                
                                                """)
                liste = list()
                for item in result:
                    model = BgpProjectsListModel()
                    model.id = item.ID
                    model.projectName = item.ProjectName
                    model.dateOfRegistiration = item.DateofRegistiration
                    model.temsilci = item.Temsilci
                    if(item.Temsilci == 19):
                        model.borderColor = 'red'
                    elif item.Temsilci == 44:
                        model.borderColor = 'blue'
                    model.ulkeAdi = item.UlkeAdi
                    model.ulkeLogo = item.UlkeLogo
                    model.filelink = item.Filelink
                    model.fileCloud = item.FileCloud
                    liste.append(model)
                schema = BgpProjectsListSchema(many=True)
                return schema.dump(liste)
            
        except Exception as e:
            print('getBgpProjectList',str(e))
            return False
        
    def getBgpProjectListAyrinti(self,projectName):
        try:
            result =  self.data.getStoreList("""
                                        select * from BgpProjectDetailList where ProjectName = ?
                                   """,(projectName))
            
            liste = list()
            for item in result:
               model = BgpProjectsAyrintiModel()
               model.id = item.ID
               model.projectName = item.ProjectName
               model.firmaAdi = item.FirmaAdi
               model.kayitTarihi = item.KayitTarihi
               model.baslik = item.Baslik
               model.aciklama = item.Aciklama
               model.hatirlatmaAciklama = item.HatirlatmaAciklama
               model.hatirlatmaTarihi = item.HatirlatmaTarihi
               model.temsilci = item.Temsilci
               model.email = item.Email
               model.phoneNumber = item.PhoneNumber
               model.wrongNumber = item.WrongNumber
               model.notResponse = item.NotResponse
               model.notInterested = item.NotInterested
               model.interested = item.Interested,
               if item.Unvan == 'contractor':
                   model.unvanColor = 'red'
               elif item.Unvan == 'architect':
                   model.unvanColor = 'Yellow'
               else:
                   model.unvanColor = 'white'
               model.unvan = item.Unvan
               liste.append(model)
            schema = BgpProjectsAyrintiSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print('getBgpProjectList hata',str(e))
            return False
        
        
    def setBgpProjectListDetail(self,datas):
        try:
            self.data.update_insert("""
                                             
                                                insert into BgpProjectDetailList
                                                (
                                                    ProjectName,
                                                    FirmaAdi,
                                                    KayitTarihi,
                                                    Baslik,
                                                    Aciklama,
                                                    HatirlatmaTarihi,
                                                    HatirlatmaAciklama,
                                                    Temsilci,
                                                    Email,
                                                    PhoneNumber,
                                                    WrongNumber,
                                                    NotResponse,
                                                    NotInterested,
                                                    Interested,
                                                    Unvan,
                                                    UlkeAdi
                                                    ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                                             
                                             
                                             """,(datas['projectName'],
                                                  datas['firmaAdi'],
                                                  datas['date'],
                                                  datas['baslik'],
                                                  datas['aciklama'],
                                                  datas['date_hatirlatma'],
                                                  datas['hatirlatma_notu'],
                                                  datas['temsilci'],
                                                  datas['email'],
                                                  datas['phoneNumber'],
                                                  datas['wrongNumber'],
                                                  datas['notResponse'],
                                                  datas['notInterested'],
                                                  datas['interested'],datas['unvan'],datas['ulkeAdi']
                                                  
                                                  
                                                  
                                                  ))
            result = self.getBgpProjectListAyrinti(datas['projectName'])
            return True,result
        except Exception as e:
            print('setBgpProjectListDetail',str(e))
            
            
    def getBgpProjectDetailForm(self,id):
        try:
            result = self.data.getStoreList("""
                                                select * from BgpProjectDetailList where ID=?
                                            
                                            """,(id))
            liste = list()
            for item in result:
               model = BgpProjectsAyrintiModel()
               model.id = item.ID
               model.projectName = item.ProjectName
               model.firmaAdi = item.FirmaAdi
               model.kayitTarihi = item.KayitTarihi
               model.baslik = item.Baslik
               model.aciklama = item.Aciklama
               model.hatirlatmaAciklama = item.HatirlatmaAciklama
               model.hatirlatmaTarihi = item.HatirlatmaTarihi
               model.temsilci = item.Temsilci
               model.email = item.Email
               model.phoneNumber = item.PhoneNumber
               model.wrongNumber = item.WrongNumber
               model.notResponse = item.NotResponse
               model.notInterested = item.NotInterested
               model.interested = item.Interested
               if item.Unvan == 'contractor':
                   model.unvanColor = 'red'
               elif item.Unvan == 'architect':
                   model.unvanColor = 'Yellow'
               else:
                   model.unvanColor = 'white'
               model.unvan = item.Unvan
               model.filelink = item.Filelink
               model.fileStatus = item.FileCloud
               liste.append(model)
            schema = BgpProjectsAyrintiSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getBgpProjectDetailForm',str(e))
            return False
        
        
    def setBgpProjectDetailFormChange(self,datas):
        try:
            self.data.update_insert("""
                                    update BgpProjectDetailList
                                        SET
                                          
                                        FirmaAdi =?,
                                        KayitTarihi =?,
                                        Baslik =?,
                                        Aciklama =?,
                                        HatirlatmaTarihi =?,
                                        HatirlatmaAciklama =?,
                                        Email=?,
                                        PhoneNumber=?,
                                        WrongNumber=?,
                                        NotResponse=?,
                                        NotInterested=?,
                                        Interested=?,
                                        Unvan=?
                                        
                                        WHERE ID=?
                                    
                                    """,(datas['firmaAdi'],
                                         datas['kayitTarihi'],
                                         datas['baslik'],
                                         datas['aciklama'],
                                         datas['hatirlatmaTarihi'],
                                         datas['hatirlatmaAciklama'],
                                         datas['email'],
                                         datas['phoneNumber'],
                                         datas['wrongNumber'],
                                         datas['notResponse'],
                                         datas['notInterested'],
                                         datas['interested'],
                                         datas['unvan'],
                                         datas['id']))
            result = self.getBgpProjectListAyrinti(datas['projectName'])
            return True,result
        except Exception as e:
            print('getBgpProjectDetailFormChange',str(e))
            result = self.getBgpProjectListAyrinti(datas['projectName'])
            return False,result
        
        
    def setBgpProjectDetailFormDelete(self,id,projectName):
        try:
            self.data.update_insert("""
                                        delete BgpProjectDetailList where ID=?
                                   
                                   """,(id))
            result = self.getBgpProjectListAyrinti(projectName)
            return True,result
        except Exception as e:
            print('setBgpProjectDetailFormDelete',str(e))
            result = self.getBgpProjectListAyrinti(projectName)
            return False,result
        
    def setBgpProjectDelete(self,temsilci,projectName):
        try:
            self.data.update_insert("""
                                        delete BgpNetworkProjects where ProjectName=?
                                    
                                    """,(projectName))
            result2 = self.data.getStoreList("""
                                        select * from BgpProjectDetailList where ProjectName=?
                                   
                                   """,(projectName))
            if len(result2)>0:
                self.data.update_insert("""
                                            delete BgpProjectDetailList where ProjectName=?
                                        
                                        """,(projectName))
            
            
            result = self.getBgpProjectList(temsilci)
            
            return True,result
        except Exception as e:
            print('setBgpProjectDelete hata',str(e))
            return False
    
    def getUlkeList(self,id):
        if id == 10:
            result = self.data.getList(
            """
            select 


                        UlkeAdi 


                    from 


                    BgpProjectDetailList 



                    group by
                        UlkeAdi
            """
            )

            liste = list()
            for item in result:
                model = BgpProjectsCountryListModel()
                model.ulkeAdi = item.UlkeAdi
                liste.append(model)
            schema = BgpProjectsCountryListSchema(many=True)
            return schema.dump(liste)
        else:
            result = self.data.getStoreList(
                """
                select 


                            UlkeAdi 


                        from 


                        BgpProjectDetailList 


                        where Temsilci=?

                        group by
                            UlkeAdi
                """,(id)
                )

            liste = list()
            for item in result:
                model = BgpProjectsCountryListModel()
                model.ulkeAdi = item.UlkeAdi
                liste.append(model)
            schema = BgpProjectsCountryListSchema(many=True)
            return schema.dump(liste)
    
    def getBgpProjectsHatirlatmaList(self,userId):
        
        try:
            result = self.data.getStoreList("""
                                            select * from 
                                            BgpProjectDetailList 
                                            where YEAR(HatirlatmaTarihi) = YEAR(GETDATE()) and
                                            MONTH(HatirlatmaTarihi) >= MONTH(GETDATE()) and
                                            DAY(HatirlatmaTarihi) >= DAY(GETDATE()) and
                                            Temsilci=?
                                       """,(userId))
            liste = list()
            for item in result:
                model = BgpProjectsAyrintiModel()
                model.id = item.ID
                model.projectName = item.ProjectName
                model.firmaAdi = item.FirmaAdi
                model.kayitTarihi = item.KayitTarihi
                model.baslik = item.Baslik
                model.aciklama = item.Aciklama
                model.hatirlatmaAciklama = item.HatirlatmaAciklama
                model.hatirlatmaTarihi = item.HatirlatmaTarihi
                model.temsilci = item.Temsilci
                model.email = item.Email
                model.phoneNumber = item.PhoneNumber
                liste.append(model)

            schema = BgpProjectsAyrintiSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getBgpProjectsHatirlatmaList',str(e))
            return False
        
    def getBgpProjectCompanyList(self):
        try:
            result = self.data.getList("""
                                                select * from BgpProjectDetailList
                                            
                                            """)
            liste = list()
            for item in result:
               model = BgpProjectsAyrintiModel()
               model.id = item.ID
               model.projectName = item.ProjectName
               model.firmaAdi = item.FirmaAdi
               model.kayitTarihi = item.KayitTarihi
               model.baslik = item.Baslik
               model.aciklama = item.Aciklama
               model.hatirlatmaAciklama = item.HatirlatmaAciklama
               model.hatirlatmaTarihi = item.HatirlatmaTarihi
               model.temsilci = item.Temsilci
               model.email = item.Email
               model.phoneNumber = item.PhoneNumber
               model.wrongNumber = item.WrongNumber
               model.notResponse = item.NotResponse
               model.notInterested = item.NotInterested
               model.interested = item.Interested
               model.unvan = item.Unvan
               
               liste.append(model)
            schema = BgpProjectsAyrintiSchema(many=True)
            return schema.dump(liste)
        except Exception as e:
            print('getBgpProjectCompanyList',str(e))
            return False
        
    def getBgpProjectCompanyStatus(self,username):
        
        if username == 19 or username == 44:
                ulkeler = self.data.getStoreList("""
                            select 
                                bgp.UlkeAdi as UlkeAdi
                            from
                                BgpProjectDetailList bgp
                            where bgp.Temsilci=?
                            
                            group by 
                                bgp.UlkeAdi
                          """,(username))
                ayrintiList = self.data.getStoreList("""
                                                    select bgp.WrongNumber,
                                                    bgp.NotResponse,
                                                    bgp.NotInterested,
                                                    bgp.Interested,
                                                    bgp.UlkeAdi 
                                                    from  BgpProjectDetailList bgp
                                                    where  (bgp.WrongNumber=1 or bgp.NotResponse=1 or bgp.Interested = 1 or bgp.NotInterested=1) and bgp.Temsilci = ?

                                                """,(username))
                liste = list()
                wrongNumber= 0
                notResponse = 0
                notInterested = 0
                interested = 0
                sumWrongNumber = 0
                sumNotResponse = 0
                sumNotInterested = 0
                sumInterested = 0
                for item in ulkeler:
                    for item2 in ayrintiList:
                        if item.UlkeAdi == item2.UlkeAdi:
                            if item2.WrongNumber == True:
                                wrongNumber += 1
                            elif item2.NotResponse == True:
                                notResponse += 1
                            elif item2.NotInterested == True:
                                notInterested += 1
                            elif item2.Interested == True:
                                interested += 1
                            else:
                                continue
                        else:
                             continue
                        
                    liste.append({'ulkeAdi':item.UlkeAdi,'wrongNumber':wrongNumber,'notResponse':notResponse,'notInterested':notInterested,'interested':interested})
                    wrongNumber= 0
                    notResponse = 0
                    notInterested = 0
                    interested = 0
                    
                
                
                
                for item2 in ayrintiList:
                        if item2.WrongNumber == True:
                            sumWrongNumber += 1
                        elif item2.NotResponse == True:
                            sumNotResponse += 1
                        elif item2.NotInterested == True:
                            sumNotInterested += 1
                        elif item2.Interested == True:
                            sumInterested += 1
                        else:
                            continue
                    

                   
                
                
                labelsData=[""]
                basicData= {
                        'labels': labelsData,
                        'datasets': [
                            {      
                                'type': 'bar',
                                'label': 'Yanlış Numara',
                                'backgroundColor': '#42A5F5',
                                'data': [sumWrongNumber]
                            },
                            {
                                'type': 'bar',
                                'label': 'Cevap Yok',
                                'backgroundColor': '#ec5552',
                                'data': [sumNotResponse]
                            },
                            {
                                'type': 'bar',
                                'label': 'İlgilenmeyen',
                                'backgroundColor': '#ffff33',
                                'data': [sumNotInterested]
                            },
                            {
                                'type': 'bar',
                                'label': 'İlgili',
                                'backgroundColor': '#28d09e',
                                'data': [ sumInterested]
                            },
                        ]
                    }
                
                
                
                
                return liste,basicData
            
        else:
            ulkeler = self.data.getList("""
                            select 
                                bgp.UlkeAdi as UlkeAdi
                            from
                                BgpProjectDetailList bgp
                            
                            group by 
                                bgp.UlkeAdi
                          """)
            ayrintiList = self.data.getList("""
                                                    select bgp.WrongNumber,
                                                        bgp.NotResponse,
                                                        bgp.NotInterested,
                                                        bgp.Interested,
                                                        bgp.UlkeAdi 
                                                        from  BgpProjectDetailList bgp

                                                    where (bgp.WrongNumber=1 or bgp.NotResponse=1 or bgp.Interested = 1 or bgp.NotInterested=1)

                                                """)
            liste = list()
            wrongNumber= 0
            notResponse = 0
            notInterested = 0
            interested = 0
            sumWrongNumber = 0
            sumNotResponse = 0
            sumNotInterested = 0
            sumInterested = 0
            for item in ulkeler:
                for item2 in ayrintiList:
                    if item.UlkeAdi == item2.UlkeAdi:
                        if item2.WrongNumber == True:
                            wrongNumber += 1
                        elif item2.NotResponse == True:
                            notResponse += 1
                        elif item2.NotInterested == True:
                            notInterested += 1
                        elif item2.Interested == True:
                            interested += 1
                        else:
                            continue
                    else:
                        continue

                liste.append({'ulkeAdi':item.UlkeAdi,'wrongNumber':wrongNumber,'notResponse':notResponse,'notInterested':notInterested,'interested':interested})
                wrongNumber= 0
                notResponse = 0
                notInterested = 0
                interested = 0
                
            
            for item2 in ayrintiList:
                if item2.WrongNumber == True:
                    sumWrongNumber += 1
                elif item2.NotResponse == True:
                    sumNotResponse += 1
                elif item2.NotInterested == True:
                    sumNotInterested += 1
                elif item2.Interested == True:
                    sumInterested += 1
                else:
                    continue
                
            
            labelsData=[""]
            basicData= {
                    'labels': labelsData,
                    'datasets': [
                        {      
                            'type': 'bar',
                            'label': 'Yanlış Numara',
                            'backgroundColor': '#42A5F5',
                            'data': [sumWrongNumber]
                        },
                        {
                            'type': 'bar',
                            'label': 'Cevap Yok',
                            'backgroundColor': '#ec5552',
                            'data': [sumNotResponse]
                        },
                        {
                            'type': 'bar',
                            'label': 'İlgilenmeyen',
                            'backgroundColor': '#ffff33',
                            'data': [sumNotInterested]
                        },
                        {
                            'type': 'bar',
                            'label': 'İlgili',
                            'backgroundColor': '#28d09e',
                            'data': [ sumInterested]
                        },
                    ]
                }
            
            
            
            
            return liste,basicData
            

    def getBgpProjectCompanyStatusDetail(self,ulkeAdi):
        try:
            result = self.data.getStoreList("""
                                                select 

                                                        * 


                                                    from BgpProjectDetailList bgp

                                                    where bgp.UlkeAdi=? and (bgp.WrongNumber=1 or bgp.NotInterested=1 or bgp.NotResponse = 1 or bgp.Interested=1) 
                                            
                                            """,(ulkeAdi))
            
            liste = list()
            for item in result:
               model = BgpProjectsAyrintiModel()
               model.id = item.ID
               model.projectName = item.ProjectName
               model.firmaAdi = item.FirmaAdi
               model.kayitTarihi = item.KayitTarihi
               model.baslik = item.Baslik
               model.aciklama = item.Aciklama
               model.hatirlatmaAciklama = item.HatirlatmaAciklama
               model.hatirlatmaTarihi = item.HatirlatmaTarihi
               model.temsilci = item.Temsilci
               model.email = item.Email
               model.phoneNumber = item.PhoneNumber
               model.wrongNumber = item.WrongNumber
               model.notResponse = item.NotResponse
               model.notInterested = item.NotInterested
               model.interested = item.Interested
               model.unvan = item.Unvan
               
               liste.append(model)
            schema = BgpProjectsAyrintiSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print('getBgpProjectCompanyStatusDetail hata',str(e))
            return False
            
    
    def getBgpProjectsCompanyDetailList(self):
        result = self.data.getList("""
                                        select 

                                            bgp.FirmaAdi 

                                        from BgpProjectDetailList bgp group by bgp.FirmaAdi
                                   
                                   """)
        liste = list()
        for item in result:
            model = BgpProjectsCompanyDetailListModel()
            model.firmaAdi = item.FirmaAdi
            liste.append(model)
        schema = BgpProjectsCompanyDetailListSchema(many=True)
        return schema.dump(liste)
    
    
    
    def getBgpProjectsCompanySelectedDetailList(self,firmaAdi):
        try:
            result =  self.data.getStoreList("""
                                        select * from BgpProjectDetailList where FirmaAdi = ?
                                   """,(firmaAdi))
            
            liste = list()
            for item in result:
               model = BgpProjectsAyrintiModel()
               model.id = item.ID
               model.projectName = item.ProjectName
               model.firmaAdi = item.FirmaAdi
               model.kayitTarihi = item.KayitTarihi
               model.baslik = item.Baslik
               model.aciklama = item.Aciklama
               model.hatirlatmaAciklama = item.HatirlatmaAciklama
               model.hatirlatmaTarihi = item.HatirlatmaTarihi
               model.temsilci = item.Temsilci
               model.email = item.Email
               model.phoneNumber = item.PhoneNumber
               model.wrongNumber = item.WrongNumber
               model.notResponse = item.NotResponse
               model.notInterested = item.NotInterested
               model.interested = item.Interested
               model.unvan = item.Unvan
               liste.append(model)
            schema = BgpProjectsAyrintiSchema(many=True)
            return schema.dump(liste)
            
        except Exception as e:
            print('getBgpProjectsCompanyDetailList hata',str(e))
            return False
        
        
        
        
    def getBgpProjectCountryandReseptation(self):
        result = self.data.getList("""
                            select 

                                count(bgp.UlkeAdi) as SumProject,
                                bgp.Temsilci as TemsilciId,
                                bgp.UlkeAdi as UlkeAdi,
                                (select k.KullaniciAdi from KullaniciTB k where k.ID = bgp.Temsilci) as TemsilciAdi


                            from BgpProjectDetailList bgp

                            group by
                                bgp.Temsilci,bgp.UlkeAdi
                          
                          """)
        liste = list()
        for item in result:
            model = BgpProjectsCountryandReseptationModel()
            model.temsilci = item.TemsilciAdi
            model.temsilciId = item.TemsilciId
            model.ulkeAdi = item.UlkeAdi
            model.projectSum = item.SumProject
            liste.append(model)
            
        schema = BgpProjectsCountryandReseptationSchema(many=True)
        return schema.dump(liste)
    
    
    def getCountryList(self):
        result = self.data.getList("""
                                   select count(bgp.UlkeAdi),bgp.UlkeAdi as UlkeAdi from BgpProjectDetailList bgp group by bgp.UlkeAdi

                                   """)
        liste = list()
        for item in result:
            model = BgpProjectsCountryListModel()
            model.ulkeAdi = item.UlkeAdi
            liste.append(model)
        schema = BgpProjectsCountryListSchema(many=True)
        return schema.dump(liste)
    
    def setFileData(self,data):
        try:
            self.data.update_insert("""
                                        update BgpNetworkProjects SET Filelink=?,FileCloud=? where ID=?

                                    """,(data['link'],True,data['id']))

            return True
        except Exception as e:
            print("setFileData hata",str(e))
            return False