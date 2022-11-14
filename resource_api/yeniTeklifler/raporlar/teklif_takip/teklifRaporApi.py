from resource_api.yeniTeklifler.raporlar.teklif_takip.teklifListe import TeklifListe
from flask_restful import Resource
from flask import jsonify


class TeklifListeGrafikApi(Resource): 

    def get(self):

        teklif = TeklifListe()

        labels,datasets = teklif.getGrafikRaporHepsi()
        datasets_oncelik,labels_oncelik = teklif.getOncelikGrafikRapor()

        data = {

            'labels' : labels,
            'datasets' : datasets,
            'datasets_oncelik' : datasets_oncelik,
            'labels_oncelik' : labels_oncelik
        }

        return jsonify(data)

class TeklifOncelikGrafikRaporList(Resource):

    def get(self):

        islem = TeklifListe()

        datasets,labels = islem.getOncelikGrafikRapor()

        data = {

            "datasets" : datasets,
            "labels" : labels
        }

        return jsonify(data)

