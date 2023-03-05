# class Animal:
#     def __init__(self, name: str) -> None:
#         self.name = name
        
#     def speak(self) -> None:
#         print(f"This animal {self.name} make a sound.")
        
# class Cow(Animal):
#     def speak(self) -> None:
#         print(self.name, "says Mooooo!")

# class Cat(Animal):
#     def speak(self) -> None:
#         print(self.name, "says Meow!")


# animal = Animal("voice")
# dog = Cow("Rose")
# cat = Cat("Garfild")

# animal.speak()
# dog.speak()
# cat.speak()





class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
        
    def calculate_bonus(self) -> float:
        return self.salary * 0.1
        
class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int) -> None:
        super().__init__(name, salary)
        self.team_size = team_size
        
    def calculate_bonus(self) -> float:
        return super().calculate_bonus() + self.team_size * 1000
        
class SalesPerson(Employee):
    def __init__(self, name: str, salary: float, sales: float) -> None:
        super().__init__(name, salary)
        self.sales = sales
        
    def calculate_bonus(self) -> float:
        if self.sales >= 100000:
            return super().calculate_bonus() + 5000
        else:
            return super().calculate_bonus()


employee = Employee("Antanas Fontanas", 50000)
manager = Manager("Jonas Jonaitis", 80000, 10)
salesperson = SalesPerson("Petras Petraitis", 60000, 120000)

print(f"{employee.name} bonus = {employee.calculate_bonus()}")
print(f"{manager.name} bonus = {manager.calculate_bonus()}")
print(f"{salesperson.name} bonus = {salesperson.calculate_bonus()}")
