import logging
from typing import List, Dict

logging.basicConfig(filename="coffee_shop.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s")

class CoffeeShop:
    def __init__(self, name: str, menu: List[Dict[str, str]], orders: List[str]) -> None:
        self.name = name
        self.menu = menu
        self.orders = orders

    def add_order(self, item: str) -> str:
        try:
            found = False
            for i in self.menu:
                if i["item"] == item:
                    self.orders.append(item)
                    found = True
                    break

            if found:
                logging.info(f"Order added: {item}")
                return "Order added!"
            else:
                logging.warning(f"Item not found: {item}")
                return "This item is currently unavailable!"
        except Exception as e:
            logging.error(f"Error occurred while adding order: {e}")
            return "An error occurred while adding your order. Please try again later."

    def fulfill_order(self) -> str:
        try:
            while self.orders:
                order = self.orders.pop(0)
                logging.info(f"Fulfilled order: {order}")
                print(f"The {order} is ready!")
            logging.info("All orders have been fulfilled")
            return "All orders have been fulfilled!"
        except Exception as e:
            logging.error(f"Error occurred while fulfilling order: {e}")
            return "An error occurred while fulfilling your order. Please try again later."

    def list_orders(self) -> List[str]:
        return self.orders

    def due_amount(self) -> float:
        total = 0
        for i in self.menu:
            if i['item'] in self.orders:
                total += float(i['price'])
        logging.info(f"Due amount: {total}")
        return round(total, 2)

    def cheapest_item(self) -> str:
        cheapest = self.menu[0]['item']
        cheapest_price = float(self.menu[0]['price'])

        for i in range(1, len(self.menu)):
            if float(self.menu[i]['price']) < cheapest_price:
                cheapest = self.menu[i]['item']
                cheapest_price = float(self.menu[i]['price'])

        logging.info(f"Cheapest item: {cheapest}")
        return cheapest

    def drinks_only(self) -> List[str]:
        drinks = []
        for i in self.menu:
            if i['type'] == 'drink':
                drinks.append(i['item'])
        return drinks

    def food_only(self) -> List[str]:
        food = []
        for i in self.menu:
            if i['type'] == 'food':
                food.append(i['item'])
        return food


tcs = CoffeeShop(
    "Tesha's coffee shop",
    [
        {"item": "orange juice", "type": "drink", "price": "0.99"},
        {"item": "lemonade", "type": "drink", "price": "1.99"},
        {"item": "cranberry juice", "type": "drink", "price": "2.99"},
        {"item": "pineapple juice", "type": "drink", "price": "3.99"},
        {"item": "lemon iced tea", "type": "drink", "price": "1.50"},
        {"item": "vanilla chai latte", "type": "drink", "price": "4.99"},
        {"item": "hot chocolate", "type": "drink", "price": "2.50"},
        {"item": "iced coffee", "type": "drink", "price": "2.50"},
        {"item": "tuna sandwich", "type": "food", "price": "3.99"},
        {"item": "ham and cheese sandwich", "type": "food", "price": "4.50"},
        {"item": "bacon and egg", "type": "food", "price": "5.55"},
        {"item": "steak", "type": "food", "price": "12.99"},
        {"item": "hamburger", "type": "food", "price": "8.99"},
        {"item": "cinnamon roll", "type": "food", "price": "3.25"},
    ],
    []
)

print(tcs.add_order("hot cocoa"))
print(tcs.add_order("iced tea"))
print(tcs.add_order("cinnamon roll"))
print(tcs.add_order("iced coffee"))
print(tcs.list_orders())
print(tcs.cheapest_item())
print(tcs.fulfill_order())
