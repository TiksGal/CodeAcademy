from pymongo import MongoClient
from datetime import datetime, timedelta
import random
from tqdm import tqdm
from random_word import RandomWords
from typing import Dict, Union

class MongoPopulator:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")  # Correct port
        self.db = self.client["grocery_store"]
        self.r = RandomWords()

    def get_random_word(self):
        return self.r.get_random_word()

    def populate(self, category, fields: Dict[str, str], num_docs):
        collection = self.db[category]
        # Remove the unique index on 'name' to avoid DuplicateKeyError
        collection.drop_indexes()

        for _ in tqdm(range(num_docs), desc=f"Generating Documents for {category}"):
            doc: Dict[str, Union[str, int, float, datetime]] = {}
            for field, field_type in fields.items():
                if field_type == "string":
                    doc[field] = self.get_random_word()  # Unique values
                elif field_type == "int":
                    doc[field] = random.randint(1, 100)
                elif field_type == "float":
                    doc[field] = round(random.uniform(1.0, 200.0), 2)
                elif field_type == "date":
                    # generate a random date in the last 5 years
                    start_date = datetime.now() - timedelta(days=5*365)
                    random_date = start_date + timedelta(days=random.randint(1, 5*365))
                    doc[field] = random_date
            collection.insert_one(doc)

        print(f"\nInserted {num_docs} documents into the {category} collection.")

if __name__ == "__main__":
    populator = MongoPopulator()
    fields = {
        "name": "string",
        "price": "float",
        "quantity": "int",
        "year_made": "date"
    }
    categories = ["electronics", "fruits", "food"]
    for category in categories:
        populator.populate(category, fields, 20)


