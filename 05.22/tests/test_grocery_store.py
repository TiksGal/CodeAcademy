import unittest
from datetime import datetime, timedelta
from pymongo import MongoClient
from typing import List, Union, Dict, Optional
from task_three_tests import get_average_price, get_electronics_value, get_items_starting_with_a, get_expensive_items, get_items_under_price_quantity, get_average_price_under_price_quantity, get_items_by_quantity


class TestGroceryStoreFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.client: MongoClient = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["grocery_store"]

    def tearDown(self) -> None:
        self.client.drop_database("grocery_store")
        self.client.close()

    def test_get_electronics_value(self) -> None:
        # Add test data to the "electronics" collection
        self.db.electronics.insert_many([
            {"name": "TV", "price": 1000, "quantity": 2, "year_made": datetime.utcnow() - timedelta(days=365)},
            {"name": "Laptop", "price": 1500, "quantity": 1, "year_made": datetime.utcnow() - timedelta(days=400)},
            {"name": "Phone", "price": 500, "quantity": 3, "year_made": datetime.utcnow() - timedelta(days=700)}
        ])

        # Call the function and get the result
        result: Union[int, None] = get_electronics_value()

        # Assert that the result matches the expected value
        expected: Union[int, None] = 3500
        self.assertEqual(result, expected)

    def test_get_average_price(self) -> None:
        # Add test data to the "electronics", "fruits", and "food" collections
        self.db.electronics.insert_many([
            {"name": "TV", "price": 1000},
            {"name": "Laptop", "price": 1500},
            {"name": "Phone", "price": 500}
        ])
        self.db.fruits.insert_many([
            {"name": "Apple", "price": 2},
            {"name": "Banana", "price": 3},
            {"name": "Orange", "price": 4}
        ])
        self.db.food.insert_many([
            {"name": "Bread", "price": 1},
            {"name": "Milk", "price": 2},
            {"name": "Eggs", "price": 3}
        ])

        # Call the function and get the results
        results: List[Union[int, float]] = get_average_price()

        # Assert that the results match the expected values
        expected: List[Union[int, float]] = [1000.0, 3.0, 2.0]
        self.assertEqual(results, expected)
        
    def test_get_items_under_price_quantity(self) -> None:
        self.db.electronics.insert_one({"name": "Earbuds", "price": 19.99, "quantity": 10, "year_made": datetime.utcnow()})
        self.db.fruits.insert_one({"name": "Apple", "price": 0.99, "quantity": 5, "year_made": datetime.utcnow()})
        items = get_items_under_price_quantity()
        self.assertEqual(len(items), 2)

    def test_get_average_price_under_price_quantity(self) -> None:
        self.db.electronics.insert_one({"name": "Earbuds", "price": 19.99, "quantity": 10, "year_made": datetime.utcnow()})
        self.db.fruits.insert_one({"name": "Apple", "price": 0.99, "quantity": 5, "year_made": datetime.utcnow()})
        average_price = get_average_price_under_price_quantity()
        self.assertAlmostEqual(average_price, (19.99 + 0.99) / 2)

    def test_get_items_by_quantity(self) -> None:
        self.db.electronics.insert_one({"name": "TV", "price": 500, "quantity": 5})
        self.db.electronics.insert_one({"name": "Laptop", "price": 1000, "quantity": 10})
        self.db.fruits.insert_one({"name": "Apple", "price": 0.99, "quantity": 15})
        items = get_items_by_quantity()
        self.assertEqual(len(items), 3)


if __name__ == '__main__':
    unittest.main()