from pymongo import MongoClient
from pymongo.errors import PyMongoError
from pymongo.errors import OperationFailure, WriteError, InvalidOperation
from pymongo.errors import ServerSelectionTimeoutError
from datetime import datetime, timedelta
import random
from tqdm import tqdm
from random_word import RandomWords
from typing import Dict, Union

class MongoPopulator:
    def __init__(self):
        try:
            self.client = MongoClient("mongodb://localhost:27017/")
            self.db = self.client["grocery_store"]
        except (PyMongoError, ServerSelectionTimeoutError) as e:
            print('An error occurred:', str(e))
            self.client = None
        self.r = RandomWords()

    def get_random_word(self):
        return self.r.get_random_word()

    def populate(self, category, fields: Dict[str, str], num_docs):
        if self.client is None:
            print("Failed to connect to MongoDB.")
            return

        collection = self.db[category]
        collection.drop_indexes()

        for _ in tqdm(range(num_docs), desc=f"Generating Documents for {category}"):
            doc: Dict[str, Union[str, int, float, datetime]] = {}
            for field, field_type in fields.items():
                if field_type == "string":
                    doc[field] = self.get_random_word() # Unique values
                elif field_type == "int":
                    doc[field] = random.randint(1, 100)
                elif field_type == "float":
                    doc[field] = round(random.uniform(1.0, 200.0), 2)
                elif field_type == "date":
                    # generate a random date in the last 5 years
                    start_date = datetime.now() - timedelta(days=5 * 365)
                    random_date = start_date + timedelta(days=random.randint(1, 5 * 365))
                    doc[field] = random_date
            try:
                collection.insert_one(doc)
            except WriteError as e:
                print("Write error:", str(e))
            except OperationFailure as e:
                print("Operation failure:", str(e))
            except InvalidOperation as e:
                print("Invalid operation:", str(e))
            except Exception as e:
                print("An error occurred:", str(e))

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




