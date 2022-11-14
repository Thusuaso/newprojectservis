from flask_restful import Resource
from views.teklifler.bgpProject import BgpProjects
from flask import jsonify,request
class BgpProjectApi(Resource):
    def get(self,projectName,temsilci,bgpUlkeAdi,ulkeLogo):
        islem = BgpProjects()
        status,result = islem.setBgpProjectsName(projectName,temsilci,bgpUlkeAdi,ulkeLogo)
        
        return {'status':status,'result':result}
    
class BgpProjectApiList(Resource):
    def get(self,temsilci):
        islem = BgpProjects()
        result = islem.getBgpProjectList(temsilci)
        ulkeler = islem.getUlkeList()
        return {'result':result,'ulkeler':ulkeler}
    
class BgpProjectAyrintiApi(Resource):
    def get(self,projectName):
        islem = BgpProjects()
        result = islem.getBgpProjectListAyrinti(projectName)
        return result
    
class BgpProjectAyrintiSave(Resource):
    def post(self):
        data = request.get_json()
        islem = BgpProjects()
        status,result = islem.setBgpProjectListDetail(data)
        return {'status':status,'result':result}
    
class BgpProjectAyrintiForm(Resource):
    def get(self,id):
        islem = BgpProjects()
        result = islem.getBgpProjectDetailForm(id)
        return result
    
class BgpProjectAyrintiFormChange(Resource):
    def post(self):
        datas = request.get_json()
        islem = BgpProjects()
        status,result = islem.setBgpProjectDetailFormChange(datas)
        return {'status':status,'result':result}


class BgpProjectAyrintiFormDelete(Resource):
    def get(self,id,projectName):
        islem = BgpProjects()
        status,result = islem.setBgpProjectDetailFormDelete(id,projectName)
        return {'status':status,'result':result}
    
class BgpProjectDelete(Resource):
    def get(self,temsilci,projectName):
        islem = BgpProjects()
        status,result = islem.setBgpProjectDelete(temsilci,projectName)
        return {'status':status,'result':result}
        
class BgpProjectHatirlatmaListApi(Resource):
    def get(self,userId):
        islem = BgpProjects()
        result = islem.getBgpProjectsHatirlatmaList(userId)
        return {'result': result}
    
class BgpProjectCompanyListApi(Resource):
    def get(self):
        islem = BgpProjects()
        result = islem.getBgpProjectCompanyList()
        return {'result':result}

class BgpProjectCompanyStatusApi(Resource):
    def get(self,username):
        islem = BgpProjects()
        result,basicData = islem.getBgpProjectCompanyStatus(username)
        return {'result':result,'chartData':basicData}
    
class BgpProjectCompanyStatusDetailApi(Resource):
    def get(self,ulkeAdi):
        islem = BgpProjects()
        result = islem.getBgpProjectCompanyStatusDetail(ulkeAdi)
        return {'result':result}
    
class BgpProjectChangeApi(Resource):
    def get(self,projectName,temsilci,bgpUlkeAdi,ulkeLogo,projectId):
        islem = BgpProjects()
        status,result = islem.setBgpProjectsNameChange(projectName,temsilci,bgpUlkeAdi,ulkeLogo,projectId)
        
        return {'status':status,'result':result}
    
class BgpProjectCompanyDetailListApi(Resource):
    def get(self):
        islem = BgpProjects()
        result = islem.getBgpProjectsCompanyDetailList()
        return result
    
class BgpServiceSelectedCompanyApi(Resource):
    def get(self,firmaAdi):
        islem = BgpProjects()
        result = islem.getBgpProjectsCompanySelectedDetailList(firmaAdi)
        return result
    
class BgpProjectCountryListApi(Resource):
    def get(self):
        islem = BgpProjects()
        result = islem.getCountryList()
        return result
    
class BgpProjectByCountryandReseptationApi(Resource):
    def get(self):
        islem = BgpProjects()
        result = islem.getBgpProjectCountryandReseptation()
        return {'result':result}
        