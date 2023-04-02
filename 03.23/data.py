class MenuItem:
    def __init__(self, name: str, weight: str, preparation_time: int, calories: int, price: float) -> None:
        self.name = name
        self.weight = weight
        self.preparation_time = preparation_time
        self.calories = calories
        self.price = price

    def get_details(self) -> str:
        return f"{self.name}: {self.weight}g, {self.preparation_time} minutes, {self.calories} calories, ${self.price:.2f}"


class Menu:
    def __init__(self, name: str, items: dict) -> None:
        self.name = name
        self.items = items

    def display_menu(self) -> None:
        print(f"\n---{self.name} Menu---")
        for item in self.items.values():
            print(item.get_details())

    def get_item_by_name(self, name: str) -> MenuItem:
        return self.items.get(name)

        
class Table:
    def __init__(self, table_number: int, size: str, reservation_status: bool = False, reserved_by: str = None) -> None:
        self.table_number = table_number
        self.size = size
        self.reservation_status = reservation_status
        self.reserved_by = reserved_by

    def reserve(self, name: str) -> bool:
        if not self.reservation_status:
            self.reservation_status = True
            self.reserved_by = name
            return True
        return False


tables = {
    1: Table(1, "Single", True),
    2: Table(2, "Single", True),
    3: Table(3, "Single"),
    4: Table(4, "Single"),
    5: Table(5, "Single"),
    6: Table(6, "Single"),
    7: Table(7, "Single"),
    8: Table(8, "Single"),
    9: Table(9, "Single"),
    10: Table(10, "Single"),
    11: Table(11, "Double"),
    12: Table(12, "Double"),
    13: Table(13, "Double"),
    14: Table(14, "Double"),
    15: Table(15, "Double"),
    16: Table(16, "Double"),
    17: Table(17, "Family"),
    18: Table(18, "Family"),
    19: Table(19, "Family"),
    20: Table(20, "Family"),
}


breakfast_items = {
    "Bacon and eggs": MenuItem("Bacon and eggs", "300g", 10, 600, 15.99),
    "Omelette": MenuItem("Omelette", "200g", 7, 400, 10.99),
    "Croissant": MenuItem("Croissant", "100g", 5, 250, 4.99),
    "Pancakes": MenuItem("Pancakes", "250g", 15, 800, 12.99),
}

lunch_items = {
    "Hamburger": MenuItem("Hamburger", "400g", 20, 1200, 20.99),
    "Chicken sandwich": MenuItem("Chicken sandwich", "350g", 15, 900, 15.99),
    "Caesar salad": MenuItem("Caesar salad", "300g", 10, 500, 12.99),
    "Soup of the day": MenuItem("Soup of the day", "350g", 10, 600, 8.99)
}

dinner_items = {
    "Steak": MenuItem("Steak", "500g", 25, 1500, 30.99),
    "Seafood pasta": MenuItem("Seafood pasta", "400g", 20, 1200, 25.99),
    "Roasted chicken": MenuItem("Roasted chicken", "450g", 30, 1000, 22.99),
    "Vegetable stir-fry": MenuItem("Vegetable stir-fry", "350g", 15, 800, 18.99)
}

drinks_items = {
    "Orange Juice": MenuItem("Orange juice", "300ml", 2, 400, 5.99),
    "Iced tea": MenuItem("Iced tea", "350ml", 3, 100, 2.99),
    "Coffe": MenuItem("Coffe", "150ml", 5, 300, 3.99)
}

menus = {
    "Breakfast": Menu("Breakfast", breakfast_items.values()),
    "Lunch": Menu("Lunch", lunch_items.values()),
    "Dinner": Menu("Dinner", dinner_items.values()),
    "Drinks": Menu("Drinks", drinks_items.values())
}
