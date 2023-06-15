# Google is launching a network of autonomous pizza delivery drones and wants you to create 
# a flexible rewards system (Pizza Points™) that can be tweaked in the future.
# The rules are simple: if a customer has made at least N orders of at least Y price, they get a FREE pizza!
# Create a function that takes a dictionary of customers, a minimum number of orders and a minimum order price. 
# Return a list of customers that are eligible for a free pizza.

from typing import Dict, List

def pizza_points(customers: Dict[str, List[int]], min_orders: int, min_price: int) -> List[str]:
    eligible_customers = []
    
    for customer, orders in customers.items():
        eligible_orders = [order for order in orders if order >= min_price]
        
        if len(eligible_orders) >= min_orders:
            eligible_customers.append(customer)
    
    return eligible_customers

customers: Dict[str, List[int]] = {
            "Antanas": [20, 30, 40, 50],
            "Barbora": [10, 20, 30, 40],
            "Olga": [25, 50, 75, 100],
            "Titas": [5, 10, 15, 20]
        }

# eligible_customers = pizza_points(customers, 3, 40)
# print(eligible_customers)