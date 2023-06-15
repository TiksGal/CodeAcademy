# You have been asked to create a simple inventory management system for a small retail store. 
# You need to define a Product class using the dataclass module that represents a product in the store. 
# Each Product should have a unique ID, a name, a description, a price, and a quantity in  stock. 
# You also need to implement a method calculate_total_cost that calculates the total cost of a given number 
# of items of the product, taking into account any discounts that may apply.

from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    quantity: int

    def calculate_total_cost(self, num_items: int) -> float:
        total_cost = self.price * num_items
        if num_items >= 10:
            total_cost *= 0.85
        return total_cost


product1 = Product(id=1, name="Cap", description="summer friend", price=25.0, quantity=50)
total_cost = product1.calculate_total_cost(num_items=5)

print(f"Total cost for 5 items of {product1.name}: ${total_cost:.2f}")
