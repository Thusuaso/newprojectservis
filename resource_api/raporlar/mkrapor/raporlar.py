from flask import request,jsonify,send_file
from flask_restful import Resource
from views.mkraporlar.raporlar import *
from resource_api.shared.excel_liste_islem import ExcellCiktiIslem
class MkSevkSipRaporApi(Resource):
    def get(self,yil):
        islem = MkRaporlar()
        musteriBazinda = islem.mkRaporlarSevkSip(yil)
        poBazinda = islem.mkRaporlarSevkSipPo(yil)
        data = {
            'musteri':musteriBazinda,
            'po':poBazinda,
        }
        return jsonify(data)
    
class MkSevkSipRaporExcelApi(Resource):
    def get(self):
        excel_path = 'resource_api/shared/dosyalar/mk_sevk_sip_listesi.xlsx'
        return send_file(excel_path,as_attachment=True)
    
    def post(self):
        data = request.get_json()
        islem = ExcellCiktiIslem()
        status = islem.mk_sevk_sip_rapor_excel(data)
        return jsonify({'status':status})
    
    