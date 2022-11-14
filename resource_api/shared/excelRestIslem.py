from resource_api.shared.excel_liste_islem import ExcellCiktiIslem
from flask_restful import Resource
from flask import jsonify,request,send_file



class SiparisCekiListesiApi(Resource):

    def post(self):

        data_list = request.get_json()

        islem = ExcellCiktiIslem()

        result = islem.ceki_listesi_excel(data_list)

        return jsonify({'status' : result})

    def get(self):

        excel_path = 'resource_api/shared/dosyalar/ceki_listesi.xlsx'

        return send_file(excel_path,as_attachment=True)
    
    
class SiparisEtiketListesiApi(Resource):

    def get(self,etiketAdi):

        excel_path = 'resource_api/shared/dosyalar/veik' + etiketAdi + '.docx'

        return send_file(excel_path,as_attachment=True)
    