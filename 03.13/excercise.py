# Create a Person class which will have three properties:
#     Name
#     List of foods they like
#     List of foods they hate
# In this class, create the method taste():
#     It will take in a food name as a string.
#     Return {person_name} eats the {food_name}.
#     If the food is in the person's like list, add 'and loves it!' to the end.
#     If it is in the person's hate list, add 'and hates it!' to the end.
#     If it is in neither list, simply add an exclamation mark to the end.
#     p1 = Person("Sam", ["ice cream"], ["carrots"])
#     p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#     p1.taste("cheese") ➞ "Sam eats the cheese!"
#     p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"
from typing import List

class Person:
    def __init__(self, name: str, likes: List[str], hates: List[str]) -> None:
        self.name = name
        self.likes = likes
        self.hates = hates
        
    def taste(self, food: str) -> str:
        if food in self.likes:
            return f"{self.name} eats the {food} and love it!"
        elif food in self.hates:
            return f"{self.name} eats the {food} and hate it!"
        else:
            return f"{self.name} eats the {food}!"
        
p1 = Person("Sam", ["Ice cream"], ["Carrots"])
print(p1.taste("Ice cream"))
print(p1.taste("Carrots"))
print(p1.taste("cheese"))
        