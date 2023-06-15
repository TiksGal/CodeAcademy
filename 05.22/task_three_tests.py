from datetime import datetime, timedelta
from pymongo import MongoClient
from typing import List, Union, Dict, Optional


def get_electronics_value() -> Union[int, None]:
    client: MongoClient = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    date_limit: datetime = datetime.utcnow() - timedelta(days=1*365 + 2*30 + 12)
    result = db.electronics.aggregate([
        {"$match": {"year_made": {"$gt": date_limit}}},
        {"$group": {"_id": None, "total_value": {"$sum": {"$multiply": ["$price", "$quantity"]}}}}
    ])
    for res in result:
        print(f"Total Value: {res['total_value']}")
        return res["total_value"]

def get_average_price() -> List[Union[int, float]]:
    client: MongoClient = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories: List[str] = ["electronics", "fruits", "food"]
    results: List[Union[int, float]] = []
    for category in categories:
        result = db[category].aggregate([
            {"$group": {"_id": None, "average_price": {"$avg": "$price"}}}
        ])
        for res in result:
            print(f"Average Price for {category}: {res['average_price']}")
            results.append(res["average_price"])
    return results

def get_items_starting_with_a() -> List[Dict[str, Union[str, int, float]]]:
    client: MongoClient = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories: List[str] = ["electronics", "fruits", "food"]
    results: List[Dict[str, Union[str, int, float]]] = []
    for category in categories:
        result = db[category].find({"name": {"$regex": "^a", "$options": "i"}, "price": {"$gt": 10, "$lt": 100}})
        print(f"Items starting with 'a' in {category}: {[item for item in result]}")
        results.extend(result)
    return results

def get_expensive_items() -> List[Dict[str, str]]:
    client: MongoClient = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories: List[str] = ["electronics", "fruits", "food"]
    results: List[Dict[str, str]] = []
    for category in categories:
        result = db[category].find({"price": {"$gt": 40}, "quantity": {"$lt": 30}}, {"name": 1, "_id": 0})
        print(f"Expensive items in {category}: {[item for item in result]}")
        results.extend(result)
    return results

def get_items_under_price_quantity() -> List[Dict[str, Union[str, datetime]]]:
    client: MongoClient = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories: List[str] = ["electronics", "fruits", "food"]
    results: List[Dict[str, Union[str, datetime]]] = []
    for category in categories:
        result = db[category].find({"price": {"$lte": 40}, "quantity": {"$lte": 30}}, {"name": 1, "year_made": 1, "_id": 0})
        print(f"Items under certain price and quantity in {category}: {[item for item in result]}")
        results.extend(result)
    return results

def get_average_price_under_price_quantity() -> Optional[float]:
    client: MongoClient = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories: List[str] = ["electronics", "fruits", "food"]
    prices: List[Union[int, float]] = []
    for category in categories:
        docs = db[category].find({"price": {"$lte": 60.0}, "quantity": {"$lte": 50.0}}, {"price": 1, "_id": 0})
        category_prices = [doc["price"] for doc in docs]
        print(f"Prices for {category}: {category_prices}")
        prices.extend(category_prices)
    return sum(prices) / len(prices) if prices else None

def get_items_by_quantity() -> List[Dict[str, Union[str, int, float]]]:
    client: MongoClient = MongoClient("mongodb://localhost:27017/")
    db = client["grocery_store"]
    categories: List[str] = ["electronics", "fruits", "food"]
    results: List[Dict[str, Union[str, int, float]]] = []
    for category in categories:
        result = db[category].find({"quantity": {"$in": [5, 10, 15]}})
        print(f"Items by quantity in {category}: {[item for item in result]}")
        results.extend(result)
    return results

if __name__ == "__main__":
    get_electronics_value()
    get_average_price()
    get_items_starting_with_a()
    get_expensive_items()
    get_items_under_price_quantity()
    get_average_price_under_price_quantity()
    get_items_by_quantity()


# output: $ py task_three_tests.py 
# Total Value: 6489.55
# Average Price for electronics: 98.90549999999999
# Average Price for fruits: 112.35
# Average Price for food: 115.575
# Items starting with 'a' in electronics: [{'_id': ObjectId('64777e8bf2e10b814a114bd6'), 'name': 'ashir', 'price': 28.57, 'quantity': 49, 'year_made': datetime.datetime(2020, 5, 23, 20, 6, 19, 501000)}]
# Items starting with 'a' in fruits: []
# Items starting with 'a' in food: [{'_id': ObjectId('64777e9bf2e10b814a114bf7'), 'name': 'axonophorous', 'price': 62.16, 'quantity': 61, 'year_made': datetime.datetime(2021, 7, 8, 20, 6, 35, 272000)}]
# Expensive items in electronics: [{'name': 'unpreciseness'}, {'name': 'gyneolatry'}]
# Expensive items in fruits: [{'name': 'citrylidene'}, {'name': 'overstir'}, {'name': 'mesorrhine'}, {'name': 'nicene'}, {'name': 'interfemoral'}, {'name': 'sorghums'}, {'name': 'unfeverish'}]
# Expensive items in food: [{'name': 'mesked'}, {'name': 'fibrolipoma'}, {'name': 'pteridophilism'}, {'name': 'rament'}, {'name': 'interpledge'}, {'name': 'sashoon'}, {'name': 'mesocuneiform'}]
# Items under certain price and quantity in electronics: [{'name': 'alod', 'year_made': datetime.datetime(2019, 11, 18, 20, 6, 19, 54000)}]
# Items under certain price and quantity in fruits: [{'name': 'nulled', 'year_made': datetime.datetime(2018, 12, 9, 20, 6, 31, 36000)}]
# Items under certain price and quantity in food: []
# Prices for electronics: [49.48, 55.2, 5.94, 28.57]
# Prices for fruits: [37.65]
# Prices for food: [31.41, 33.01]
# Items by quantity in electronics: [{'_id': ObjectId('64777e8bf2e10b814a114bd5'), 'name': 'alod', 'price': 5.94, 'quantity': 15, 'year_made': 
# datetime.datetime(2019, 11, 18, 20, 6, 19, 54000)}]
# Items by quantity in fruits: []
# Items by quantity in food: [{'_id': ObjectId('64777e9cf2e10b814a114bf9'), 'name': 'fibrolipoma', 'price': 105.27, 'quantity': 5, 'year_made': datetime.datetime(2022, 1, 17, 20, 6, 36, 152000)}]
# (.venv) 






