from flask_restful import Resource
from flask import jsonify,request,send_file
from views.raporlar.stock_price import StockPrice
class StockPriceAddApi(Resource):

    def post(self):
        data = request.get_json()
        stockPrice = StockPrice()

        liste = stockPrice.add(data)


        return liste