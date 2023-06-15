from datetime import datetime, timedelta
from pymongo import MongoClient

def get_electronics_value():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    date_limit = datetime.utcnow() - timedelta(days=1*365 + 2*30 + 12)
    result = db.electronics.aggregate([
        {"$match": {"year_made": {"$gt": date_limit}}},
        {"$group": {"_id": None, "total_value": {"$sum": {"$multiply": ["$price", "$quantity"]}}}}
    ])
    for res in result:
        print(f"Total monetary value of electronics made after {date_limit}: {res['total_value']}")

def get_average_price():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories = ["electronics", "fruits", "food"]
    for category in categories:
        result = db[category].aggregate([
            {"$group": {"_id": None, "average_price": {"$avg": "$price"}}}
        ])
        for res in result:
            print(f"Average price for {category}: {res['average_price']}")

def get_items_starting_with_a():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories = ["electronics", "fruits", "food"]
    for category in categories:
        results = db[category].find({"name": {"$regex": "^a", "$options": "i"}, "price": {"$gt": 10, "$lt": 100}})
        for res in results:
            print(res)

def get_expensive_items():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories = ["electronics", "fruits", "food"]
    for category in categories:
        results = db[category].find({"price": {"$gt": 50}, "quantity": {"$lt": 10}}, {"name": 1, "_id": 0})
        for res in results:
            print(res)

# Execute the functions
get_electronics_value()
get_average_price()
get_items_starting_with_a()
get_expensive_items()
