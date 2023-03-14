# Create a class Smoothie and do the following:
#     Create an instance attribute called ingredients.
#     Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
#     Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
#     Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
# Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.
from typing import Union, List

class Smoothie:
    prices = {
            "spinach": 0.99,
            "grapes": 1.20,
            "banana": 0.50,
            "mango": 2.50,
            "blueberries": 1.00,
            "raspberries": 1.00,
            "apple": 1.75,
        }
    def __init__(self, ingredients: list[str]) -> None:
        self.ingredients = ingredients
        
    def get_cost(self) -> float:
        total_cost = sum(Smoothie.prices.get(ingredient, 0) for ingredient in self.ingredients)
        return round(total_cost, 2)
    
    def get_price(self) -> float:
        total_cost = self.get_cost()
        total_price = total_cost + total_cost * 1.5
        return round(total_price, 2)
    
    def get_name(self) -> str:
        ingredients = sorted(self.ingredients)
        for part in range(len(ingredients)):
            if ingredients[part].endswith("berries"):
                ingredients[part] = ingredients[part][:-7] + "berry"
        name = " ".join(ingredients)
        if len(ingredients) > 1:
            name += " fusion"
        else:
            name += " smoothie"
        return f"Enjoy your {name} !"
    
class SpinachBananaSmoothie(Smoothie):
    def __init__(self) -> None:
        ingredients = ["spinach", "banana", "mango"]
        self.ingredients = ingredients
        
class BlueberriesSmoothie(Smoothie):
    def __init__(self) -> None:
        ingredients = ["blueberries"]
        self.ingredients = ingredients
        
sb_smoothie = SpinachBananaSmoothie()
b_smoothie = BlueberriesSmoothie()
print(sb_smoothie.get_name())
print(sb_smoothie.get_cost())
print(sb_smoothie.get_price())
print(b_smoothie.get_name())
print(b_smoothie.get_cost())
print(b_smoothie.get_price())