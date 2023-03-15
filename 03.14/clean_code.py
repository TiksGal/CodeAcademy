# class person():
#     def __init__(self, name, surname):
#         self.name=name
#         self.surname=surname
#     def sayHello(self):
#         print(f"hello, {self.name}")
# PERSON = person("first", "person")
# PERSON.sayHello()
class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def say_hello(self) -> None:
        print(f"Hello, {self.name} {self.surname}!")


P1 = Person("first", "person")
P1.say_hello()

# def x(a):
#     """Function greets a person given full name as a string"""

#     print(f"Hello {a.split()[0]} {a.split()[1]}, How are you today?")
def greet_person(full_name: str) -> None:
    first_name, last_name = full_name.split()
    print(f"Hello {first_name} {last_name}, how are you today?")


greet_person("Laba Diena")


# def Greet_User (age):
#     eligiebleTo_enter = age>21
    
#     if eligiebleTo_enter == True:
#         print("Welcome")
#     if eligiebleTo_enter == False:
#         print("Access denied")

def greet_user(age: int) -> None:
    eligible_to_enter = age > 21

    if eligible_to_enter:
        print("Welcome")
    else:
        print("Access denied")

