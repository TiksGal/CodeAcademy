# Define the Animal, Mammal, and Primate classes.
# Animal should have a name attribute and a make_noise() method.
# Mammal should have a warm_blooded attribute and a give_birth() method.
# Primate should have an opposable_thumbs attribute and a swing() method.
# Test the classes by creating a Chimpanzee and making it do various things :)
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def make_noise(self):
        print(f"The {self.name} makes a noise")


class Mammal(Animal):
    def __init__(self, name: str, warm_blooded: bool) -> None:
        super().__init__(name)
        self.warm_blooded = warm_blooded
    
    def give_birth(self) -> None:
        print(f"The {self.name} gives birth")


class Primate(Mammal):
    def __init__(self, name: str, warm_blooded=True, opposable_thumbs=True) -> None:
        super().__init__(name, warm_blooded)
        self.opposable_thumbs = opposable_thumbs
    
    def swing(self) -> None:
        if self.opposable_thumbs:
            print(f"The {self.name} swings using its opposable thumbs")
        else:
            print(f"The {self.name} can't swing because it doesn't have opposable thumbs")
            

chimp = Primate("Chimpanzee")
chimp.make_noise()
chimp.swing()
