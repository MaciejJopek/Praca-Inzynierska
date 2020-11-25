from pymongo import MongoClient

class create_connection_to_database():

    def __init__(self):
        self.client = MongoClient()

        
    def connect_to_db(self):
        db = self.client.pomiary
        collection = db.czujniki_dane
        return collection


    def connect_to_db_password(self):
        db = self.client.pomiary
        collection = db.password
        return collection