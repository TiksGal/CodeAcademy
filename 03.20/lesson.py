from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def no_of_wheels(self) -> None:
        pass

class Car(Vehicle):
    def no_of_wheels(self) -> int:
        return 4

class Bike(Vehicle):
    def no_of_wheels(self) -> int:
        return 2