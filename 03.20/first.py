# Create an abstract class Animal with which takes name of animal as an input and initialize it. 
# The create speak abstract method, to be overridden by subclasses. 
# And get_name method which returns name of the animal.

# Now create two subclasses of Animals: 
# Dog and Cat which overrides the speak method, and provide the implementation which returns a string 
# "Dog says Woof!" and "Cat says Meow!" respectively.

from abc import ABC, abstractmethod

class Animals(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self)-> str:
        raise NotImplementedError

    def get_name(self)-> str:
        return self.name

class Dog(Animals):
    def speak(self)-> str:
        return print(f"Dog says Woof!")

class Cat(Animals):
    def speak(self)-> str:
        return print(f"Cat says Meow!")

dog = Dog("Toras")
cat = Cat("Garfild")

print(dog.speak())
print(dog.get_name())
print(cat.speak())
print(cat.get_name())
# output
# Dog says Woof!
# None
# Toras
# Cat says Meow!
# None
# Garfild