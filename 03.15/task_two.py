# Create a Bus, Taxi, Train child classes that inherits from the Vehicle class.
# Implement at least five methods in a superclass what would describe those vehicles.
# The default fare charge of any vehicle is seating capacity * 100 . If Vehicle is Bus
# instance, we need to add an extra 10% on full fare as a maintenance charge.

class Vehicle:
    def __init__(self, name: str, seating_capacity: int, max_speed: float) -> None:
        self.name = name
        self.seating_capacity = seating_capacity
        self.max_speed = max_speed

    def start(self) -> None:
        print(f"{self.name} has started.")

    def stop(self) -> None:
        print(f"{self.name} has stopped.")

    def accelerate(self) -> None:
        print(f"{self.name} is accelerating.")

    def brake(self) -> None:
        print(f"{self.name} is braking.")

    def fare_charge(self) -> float:
        fare = self.seating_capacity * 10
        if type(self) is Bus:
            fare *= 1.1
        return fare


class Bus(Vehicle):
    def __init__(self, name: str, seating_capacity: int, max_speed: float) -> None:
        super().__init__(name, seating_capacity, max_speed)

    def open_doors(self) -> None:
        print(f"{self.name} has opened its doors.")

    def close_doors(self) -> None:
        print(f"{self.name} has closed its doors.")


class Taxi(Vehicle):
    def __init__(self, name: str, seating_capacity: int, max_speed: float) -> None:
        super().__init__(name, seating_capacity, max_speed)

    def pay_fare(self):
        print(f"{self.name} has been paid its fare.")


class Train(Vehicle):
    def __init__(self, name: str, seating_capacity: int, max_speed: float) -> None:
        super().__init__(name, seating_capacity, max_speed)

    def load_cargo(self) -> None:
        print(f"{self.name} is loading cargo.")

    def unload_cargo(self):
        print(f"{self.name} is unloading cargo.")
        

bus = Bus("Kautra", 50, 100)
taxi = Taxi("Bolt", 4, 160)
train = Train("LG", 150, 200)

bus.start()
bus.open_doors()
bus.close_doors()
bus.accelerate()
bus.brake()
print(bus.fare_charge())

taxi.start()
taxi.accelerate()
taxi.brake()
taxi.pay_fare()
print(taxi.fare_charge())

train.start()
train.accelerate()
train.brake()
train.load_cargo()
train.unload_cargo()
print(train.fare_charge())
