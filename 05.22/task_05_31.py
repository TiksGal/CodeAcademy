import pymongo
import random
from tqdm import tqdm
from random_word import RandomWords
from typing import Dict, Union

class MongoPopulator:
    def __init__(self) -> None:
        self.client: pymongo.MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = None
        self.collection = None
        self.fields: Dict[str, str] = {}
        self.documents: int = 0
        self.r: RandomWords = RandomWords()

    def get_random_word(self) -> str:
        return self.r.get_random_word()

    def get_user_input(self) -> None:
        database = "RandomDatabase1"
        collection = "RandomCollection1"
        self.db = self.client[database]
        self.collection = self.db[collection]
        self.fields = {"word": "string", "num": "int"}
        self.documents = 20

    def populate(self) -> None:
        for _ in tqdm(range(self.documents), desc="Generating Documents"):
            doc: Dict[str, Union[str, int, float]] = {}
            for field, field_type in self.fields.items():
                if field_type == "string":
                    doc[field] = self.get_random_word()
                elif field_type == "int":
                    doc[field] = random.randint(1, 100)
            self.collection.insert_one(doc)
        print(f"\nInserted {self.documents} documents into the MongoDB collection.")
        self.print_documents()

    def print_documents(self) -> None:
        doc = self.collection.find()
        for doc in docs:
            print(doc)

    def query_with_operators(self) -> None:
        print(f"\nQuerying documents in the database '{self.db.name}' and collection '{self.collection.name}' with 'num' field between 30 and 60:")
        docs = self.collection.find({"num": {"$gte": 30, "$lte": 60}})
        for doc in docs:
            print(doc)


if __name__ == "__main__":
    populator: MongoPopulator = MongoPopulator()
    populator.get_user_input()
    populator.populate()
    populator.query_with_operators()


# output: $ py task_05_31.py 
# Generating Documents: 100%|█████████████████████████████████████████████████████████████████████████████████| 20/20 [00:10<00:00,  1.86it/s]

# Inserted 20 documents into the MongoDB collection.
# {'_id': ObjectId('647769c5b5601a2c2702f734'), 'word': 'lowable', 'num': 81}
# {'_id': ObjectId('647769c5b5601a2c2702f735'), 'word': 'inconnus', 'num': 100}
# {'_id': ObjectId('647769c6b5601a2c2702f736'), 'word': 'scrounging', 'num': 60}
# {'_id': ObjectId('647769c6b5601a2c2702f737'), 'word': 'sunstones', 'num': 76}
# {'_id': ObjectId('647769c7b5601a2c2702f738'), 'word': 'effraction', 'num': 3}
# {'_id': ObjectId('647769c8b5601a2c2702f739'), 'word': 'unshuffle', 'num': 97}
# {'_id': ObjectId('647769c8b5601a2c2702f73a'), 'word': 'impresas', 'num': 19}
# {'_id': ObjectId('647769c9b5601a2c2702f73b'), 'word': 'decimalize', 'num': 37}
# {'_id': ObjectId('647769c9b5601a2c2702f73c'), 'word': 'eaters', 'num': 43}
# {'_id': ObjectId('647769cab5601a2c2702f73d'), 'word': 'structional', 'num': 21}
# {'_id': ObjectId('647769cbb5601a2c2702f73e'), 'word': 'counterbattery', 'num': 99}
# {'_id': ObjectId('647769cbb5601a2c2702f73f'), 'word': 'nonpersuasiveness', 'num': 60}
# {'_id': ObjectId('647769ccb5601a2c2702f740'), 'word': 'supersufficiency', 'num': 83}
# {'_id': ObjectId('647769ccb5601a2c2702f741'), 'word': 'localite', 'num': 89}
# {'_id': ObjectId('647769cdb5601a2c2702f742'), 'word': 'etioporphyrin', 'num': 10}
# {'_id': ObjectId('647769cdb5601a2c2702f743'), 'word': 'redeveloping', 'num': 52}
# {'_id': ObjectId('647769cdb5601a2c2702f744'), 'word': 'monomethylated', 'num': 80}
# {'_id': ObjectId('647769ceb5601a2c2702f745'), 'word': 'metallotherapeutic', 'num': 50}
# {'_id': ObjectId('647769ceb5601a2c2702f746'), 'word': 'unblasted', 'num': 95}
# {'_id': ObjectId('647769cfb5601a2c2702f747'), 'word': 'penorcon', 'num': 22}

# Querying documents in the database 'RandomDatabase1' and collection 'RandomCollection1' with 'num' field between 30 and 60:
# {'_id': ObjectId('647769c6b5601a2c2702f736'), 'word': 'scrounging', 'num': 60}
# {'_id': ObjectId('647769c9b5601a2c2702f73b'), 'word': 'decimalize', 'num': 37}
# {'_id': ObjectId('647769c9b5601a2c2702f73c'), 'word': 'eaters', 'num': 43}
# {'_id': ObjectId('647769cbb5601a2c2702f73f'), 'word': 'nonpersuasiveness', 'num': 60}
# {'_id': ObjectId('647769cdb5601a2c2702f743'), 'word': 'redeveloping', 'num': 52}
# {'_id': ObjectId('647769ceb5601a2c2702f745'), 'word': 'metallotherapeutic', 'num': 50}
# (.venv) 