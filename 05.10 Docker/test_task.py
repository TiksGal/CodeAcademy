import unittest
from task import pizza_points
from typing import Dict, List

class TestPizzaPoints(unittest.TestCase):

    def test_eligible_customers(self) -> None:
        customers: Dict[str, List[int]] = {
            "Antanas": [20, 30, 40, 50],
            "Barbora": [10, 20, 30, 40],
            "Olga": [25, 50, 75, 100],
            "Titas": [5, 10, 15, 20]
        }

        min_orders: int = 2
        min_price: int = 30
        result: List[str] = pizza_points(customers, min_orders, min_price)
        self.assertEqual(result, ["Antanas", "Barbora", "Olga"])

    def test_no_eligible_customers(self) -> None:
        customers: Dict[str, List[int]] = {
            "Antanas": [20, 25, 30],
            "Barbora": [10, 20, 30],
            "Olga": [25, 50, 75],
            "Titas": [5, 10, 15]
        }

        min_orders: int = 3
        min_price: int = 50
        result: List[str] = pizza_points(customers, min_orders, min_price)
        self.assertEqual(result, [])

    def test_all_eligible_customers(self) -> None:
        customers: Dict[str, List[int]] = {
            "Antanas": [40, 50, 60],
            "Barbora": [50, 60, 70],
            "Olga": [60, 70, 80],
            "Titas": [70, 80, 90]
        }

        min_orders: int = 3
        min_price: int = 40
        result: List[str] = pizza_points(customers, min_orders, min_price)
        self.assertEqual(result, ["Antanas", "Barbora", "Olga", "Titas"])

if __name__ == '__main__':
    unittest.main()
