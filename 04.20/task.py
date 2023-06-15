# Create a dataclass named "Product" that has the following attributes:
#     product_id: int
#     name: str
#     price: float
#     quantity: int
# The class should also have a method named "total_cost" that calculates and returns the total cost of the product, which is the price multiplied by the quantity.
# Create a list of Product objects and write a function that takes this list as input and returns the product with the highest total cost.
# Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost.

from dataclasses import dataclass
from typing import List

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self) -> float:
        return self.price * self.quantity

def find_highest_total_cost(products: List[Product]) -> Product:
    return max(products, key=lambda p: p.total_cost())

# Creating a list of 5 Product objects
products = [
    Product(1, "Product A", 10.0, 5),
    Product(2, "Product B", 20.0, 3),
    Product(3, "Product C", 15.0, 6),
    Product(4, "Product D", 12.0, 8),
    Product(5, "Product E", 25.0, 2),
]

# Printing out their attributes
for product in products:
    print(product)

# Finding the product with the highest total cost
highest_total_cost_product = find_highest_total_cost(products)
print(f"\nThe product with the highest total cost is: {highest_total_cost_product}")
