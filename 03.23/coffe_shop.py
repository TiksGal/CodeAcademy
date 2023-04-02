from typing import List
from abc import ABC, abstractmethod
import datetime
from typing import List


class Table:
    def __init__(self, table_type: str, table_number: int):
        self.table_type = table_type
        self.table_number = table_number
        self.reserved = False
        self.reservation_name = None
        self.reservation_time = None


class Reservation:
    def __init__(self, name: str, table_type: str, reservation_time: str):
        self.name = name
        self.table_type = table_type
        self.reservation_time = reservation_time


table_types = {
    "Single": 10,
    "Double": 6,
    "Family": 4,
}

tables = []


def initialize_tables():
    table_number = 1
    for table_type, count in table_types.items():
        for i in range(count):
            table = Table(table_type, table_number)
            if i < 2:
                table.reserved = True
                table.reservation_name = f"Reserved-{table_number}"
            tables.append(table)
            table_number += 1


def get_reservations() -> List[Reservation]:
    reservations = []
    while True:
        reserved = input("Is a table reserved? (yes/no): ").lower()
        if reserved == "yes":
            name = input("Enter reservation name: ")
            table_type = input("Enter table type: ")
            reservation_time = input("Enter reservation time (YYYY-MM-DD HH:MM): ")
            reservations.append(Reservation(name, table_type, reservation_time))
        else:
            break
    return reservations


def display_tables() -> None:
    available_tables = []
    reserved_tables = []
    for table in tables:
        if table.reserved:
            reserved_tables.append(table)
        else:
            available_tables.append(table)

    print("Available Tables:")
    for table in available_tables:
        print(f"Table {table.table_number} ({table.table_type})")

    print("\nReserved Tables:")
    for table in reserved_tables:
        print(
            f"Table {table.table_number} ({table.table_type}) - {table.reservation_name}"
        )


def select_table() -> Table:
    while True:
        table_number = int(input("Enter table number: "))
        table = tables[table_number - 1]
        if not table.reserved:
            return table
        else:
            print("Table is already reserved. Please select another table")


class MenuItem(ABC):
    def __init__(
        self, name: str, weight: int, preparation_time: int, calories: int, price: float
    ):
        self.name = name
        self.weight = weight
        self.preparation_time = preparation_time
        self.calories = calories
        self.price = price

    @abstractmethod
    def get_menu_type(self) -> str:
        pass


class BreakfastMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Breakfast"


class LunchMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Lunch"


class DinnerMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Dinner"


class DrinkMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Drink"


class AlcoholMenuItem(DrinkMenuItem):
    def get_menu_type(self) -> str:
        return "Alcohol"


class AlcoholFreeMenuItem(DrinkMenuItem):
    def get_menu_type(self) -> str:
        return "Alcohol-Free"


class VegetarianMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Vegetarian"


class VeganMenuItem(MenuItem):
    def get_menu_type(self) -> str:
        return "Vegan"


class Order:
    def __init__(self) -> None:
        self.items: List[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def remove_item(self, item: MenuItem) -> None:
        self.items.remove(item)

    def update_item(self, old_item: MenuItem, new_item: MenuItem) -> None:
        index = self.items.index(old_item)
        self.items[index] = new_item

    def waiting_time(self) -> int:
        preparation_times = [item.preparation_time for item in self.items]
        max_preparation_time = max(preparation_times)
        return max_preparation_time

    def calculate_total(self) -> float:
        return sum(item.price for item in self.items)

    def add_tip(self, tip_percentage: int) -> float:
        total = self.calculate_total()
        tip_amount = total * (tip_percentage / 100)
        total_with_tip = total + tip_amount
        print(f"\nTotal with tip ({tip_percentage}%): {total_with_tip:.2f} $")
        return total_with_tip

    def generate_receipt(self, filename):
        with open(filename, "w") as file:
            file.write("Order Details:\n\n")
            for item in self.items:
                file.write(f"- {item.name} ({item.price} $)\n")
            total = self.calculate_total()
            file.write(f"\nTotal: {total} $\n")
            file.write(f"\nThank you for dining with us!")
        print(f"Receipt saved to {filename}.")


def main():
    initialize_tables()
    reservations = get_reservations()

    for reservation in reservations:
        matching_tables = [
            table
            for table in tables
            if table.table_type == reservation.table_type and not table.reserved
        ]
        if matching_tables:
            table = matching_tables[0]
            table.reserved = True
            table.reservation_name = reservation.name
            table.reservation_time = datetime.datetime.strptime(
                reservation.reservation_time, "%Y-%m-%d %H:%M"
            )
            print(
                f"Table {table.table_number} ({table.table_type}) is reserved for {table.reservation_name} at {table.reservation_time}."
            )
        else:
            print(
                f"No available table of type {reservation.table_type} for {reservation.name} at {reservation.reservation_time}."
            )

    display_tables()
    table = select_table()

    menu = [
        BreakfastMenuItem("Eggs Benedict", 200, 15, 500, 15.99),
        LunchMenuItem("Caesar Salad", 250, 10, 300, 12.99),
        DinnerMenuItem("Steak with Mashed Potatoes", 400, 25, 800, 29.99),
        AlcoholFreeMenuItem("Orange Juice", 250, 5, 100, 4.99),
        AlcoholMenuItem("Red Wine", 750, 10, 200, 19.99),
        VegetarianMenuItem("Stir Fry Vegetables", 300, 20, 400, 15.99),
        VeganMenuItem("Vegan Burger", 250, 15, 350, 12.99),
    ]

    order = Order()
    while True:
        print("\nMenu:")
        for i, item in enumerate(menu):
            print(f"{i+1}. {item.name} - {item.price} $")

        option = input("Enter option number to order or 'done' to finish ordering: ")
        if option == "done":
            break

        try:
            item = menu[int(option) - 1]
        except (ValueError, IndexError):
            print("Invalid option. Please try again.")
            continue

        order.add_item(item)
        print(f"{item.name} added to order.")

    print("\nOrder:")
    for item in order.items:
        print(f"- {item.name} ({item.price} $)")

    while True:
        modify = input("Do you want to modify the order? (yes/no): ")
        if modify == "no":
            break

        print("\nCurrent Order:")
        for i, item in enumerate(order.items):
            print(f"{i+1}. {item.name} ({item.price} $)")

        try:
            option = int(
                input("Enter option number to modify or 'done' to finish modifying: ")
            )
        except ValueError:
            print("Invalid option. Please try again.")
            continue

        if option == "done":
            break

        try:
            item = order.items[option - 1]
        except IndexError:
            print("Invalid option. Please try again.")
            continue

        new_option = input(
            "Enter new option number to replace or 'cancel' to keep the original item: "
        )
        if new_option == "cancel":
            continue

        try:
            new_item = menu[int(new_option) - 1]
        except (ValueError, IndexError):
            print("Invalid option. Please try again.")
            continue

        order.update_item(item, new_item)

    total = order.calculate_total()
    print(f"\nTotal: {total} $")

    add_tip = input("Do you want to add a tip? (yes/no): ")
    if add_tip.lower() == "yes":
        tip_percentage = int(input("Enter tip percentage: "))
        total_with_tip = order.add_tip(tip_percentage)
        print(f"\nTotal with tip ({tip_percentage}%): {total_with_tip} $")
    else:
        total_with_tip = total

    print("\nOrder:")
    for item in order.items:
        print(f"- {item.name} ({item.price} $)")

    print(f"\nTotal with tip ({tip_percentage}%): {total_with_tip} $")
    print(f"Approximate waiting time: {order.waiting_time()} minutes.")

    order.generate_receipt("order.txt")
    print("Thank you for dining with us!")


if __name__ == "__main__":
    main()
