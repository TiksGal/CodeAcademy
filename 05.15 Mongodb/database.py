from pymongo import MongoClient
from pymongo.database import Database

def get_database() -> Database:
    client = MongoClient('mongodb://localhost:27017/')
    return client['task_manager']
