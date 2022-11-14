from pymongo import MongoClient
class MongoDb:
    def __init__(self):
        client = MongoClient("mongodb://localhost:27017/")
        self.data = client.mekmarsite