from pymongo import MongoClient
from app.config import settings


class MongoDB:
    URI = settings.MONGO_DB_URL
    db = None

    @staticmethod
    def initialize():
        client = MongoClient(MongoDB.URI)
        MongoDB.db = client['test']

    @staticmethod
    def insert(collection, data):
        return MongoDB.db[collection].insert_one(data)

    @staticmethod
    def find_one(collection, query, params):
        return MongoDB.db[collection].find_one(query, params)

    @staticmethod
    def update(collection, query, update):
        return MongoDB.db[collection].update_one(query, update, upsert=True)

    @staticmethod
    def delete(collection, query):
        return MongoDB.db[collection].delete_one(query)


db = MongoDB
db.initialize()
