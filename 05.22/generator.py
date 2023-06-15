import pymongo
import random
from tqdm import tqdm
from random_word import RandomWords
from typing import Dict, Union

class MongoPopulator:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = None
        self.collection = None
        self.fields: Dict[str, str] = {}
        self.documents = 0
        self.r = RandomWords()

    def get_random_word(self):
        return self.r.get_random_word()

    def get_user_input(self):
        database = input("Enter the name of the MongoDB database: ")
        collection = input("Enter the name of the MongoDB collection: ")

        self.db = self.client[database]
        self.collection = self.db[collection]

        while True:
            field_name = input("Enter field name (or 'done' to finish): ")
            if field_name.lower() == "done":
                break
            field_type = input("Enter field type (string/int/float): ")
            self.fields[field_name] = field_type

        self.documents = int(input("Enter number of documents to create: "))

    def populate(self):
        for _ in tqdm(range(self.documents), desc="Generating Documents"):
            doc: Dict[str, Union[str, int, float]] = {}
            for field, field_type in self.fields.items():
                if field_type == "string":
                    doc[field] = self.get_random_word()
                elif field_type == "int":
                    doc[field] = random.randint(1, 100)
                elif field_type == "float":
                    doc[field] = round(random.uniform(1.0, 100.0), 2)
            self.collection.insert_one(doc)
        print(f"\nInserted {self.documents} documents into the MongoDB collection.")
        self.print_documents()

    def print_documents(self):
        docs = self.collection.find()
        for doc in docs:
            print(doc)

if __name__ == "__main__":
    populator = MongoPopulator()
    populator.get_user_input()
    populator.populate()



