from datetime import date
import datetime


class Person:
    description: str = "A simple normal human being"
        
    def __init__(self, name: str, surname: str) -> str:
        self.name: str = name
        self.surname: str = surname
        print(self.greet())
     
     
        # Hello my name is <name>
    def greet(self):
        return f"Hello my name is {self.name}"
    
    def walkaway(self):
        return f"{self.name} is walking away..."
    
    def calculate_days_left_tills_black_friday(self):
        # get today day
        # initialize black friday day
        # return black friday day - today day
        today = date.today()
        black_friday_date = datetime.date(2023, 11, 24)
        delta = black_friday_date - today
        return delta.days
    
    def get_eye_color(self, eye_color: str ="Blue") -> str:
        return eye_color
    
    def __repr__(self) -> str:
        return f"Person: {self.name}-{self.surname}"

    
person = Person("Marius", "Sertvytis")
person2 = Person("Antanas", "Fontanas")

print(person)
print(person.walkaway())
print(person2.greet())
print(person2.walkaway())

print(person.description)
print(person.calculate_days_left_tills_black_friday())
print(person.get_eye_color())
print(repr(person2))
print(repr(person))