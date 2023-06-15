from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str
    

@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
    

point = Point(3, 4)
print(point.distance_from_origin()) # Output: 5.0
