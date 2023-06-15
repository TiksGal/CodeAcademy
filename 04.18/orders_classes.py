from dataclasses import dataclass, field
from typing import Union, Dict, Optional, List
import helpers as helpers
import menu as menu_dict
from menu_class import Menu


@dataclass
class Order:
    name: str
    surname: str
    foods: Dict[str, int]
    alcohol: Dict[str, int] = None
    alcohol_free: Dict[str, int] = None
    total_cost: Union[int, float] = 0
    prep_time: int = 0


@dataclass
class Orders:
    orders: List[Order] = field(default_factory=list)

    def make_order(
        self,
        name: str,
        surname: str,
        foods: Dict[str, int],
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
    ) -> None:
        if alcohol != None and alcohol_free != None:
            self.orders.append(Order(name, surname, foods, alcohol, alcohol_free))
        if alcohol != None and alcohol_free == None:
            self.orders.append(Order(name, surname, foods, alcohol))
        if alcohol_free != None and alcohol == None:
            self.orders.append(Order(name, surname, foods, alcohol_free))

    def update_order_quantities(
        self,
        name: str,
        surname: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ) -> None:
        if helpers.is_value_not_none(alcohol):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.alcohol.update(alcohol)
        if helpers.is_value_not_none(alcohol_free):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.alcohol_free.update(alcohol_free)
        if helpers.is_value_not_none(foods):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    order.foods.update(foods)

    def remove_from_order(self, name: str, surname: str, item_to_remove: str) -> None:
        for order in self.orders:
            if order.name == name and order.surname == surname:
                if item_to_remove in menu_dict.VALID_DRINKS:
                    del order.alcohol_free[item_to_remove]
                    return
                if item_to_remove in menu_dict.VALID_FOODS:
                    del order.foods[item_to_remove]
                    return
                if item_to_remove in menu_dict.VALID_ALC_DRINKS:
                    del order.alcohol[item_to_remove]
                    return
                else:
                    print("Customer has not ordered such thing")

    def add_to_order(
        self,
        name: str,
        surname: str,
        alcohol: Dict[str, int] = None,
        alcohol_free: Dict[str, int] = None,
        foods: Dict[str, int] = None,
    ) -> None:
        if helpers.is_value_not_none(alcohol):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    for key, value in alcohol.items():
                        if order.alcohol == None:
                            order.alcohol = {}
                            order.alcohol[key] = value
                        else:
                            order.alcohol[key] = value
                else:
                    continue
        if helpers.is_value_not_none(alcohol_free):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    for key, value in alcohol_free.items():
                        if order.alcohol_free == None:
                            order.alcohol_free = {}
                            order.alcohol_free[key] = value
                        else:
                            order.alcohol_free[key] = value
                else:
                    continue
        if helpers.is_value_not_none(foods):
            for order in self.orders:
                if order.name == name and order.surname == surname:
                    for key, value in foods.items():
                        order.foods[key] = value
                else:
                    continue

    def calculate_order_cost(self, name: str, surname: str) -> None:
        full_menu = dict(
            menu_dict.VALID_ALC_DRINKS,
            **menu_dict.VALID_DRINKS,
            **menu_dict.VALID_FOODS,
        )
        for order in self.orders:
            if order.name == name and order.surname == surname:
                if order.alcohol == None:
                    full_order = dict(order.foods, **order.alcohol_free)
                if order.alcohol_free == None:
                    full_order = dict(order.foods, **order.alcohol)
                if order.alcohol_free and order.alcohol == None:
                    full_order = dict(order.foods)
                for key in full_order.keys():
                    order.total_cost += full_menu[key] * full_order[key]

    def show_order_summarized(self, name: str, surname: str) -> None:
        for order in self.orders:
            if order.name == name and order.surname == surname:
                if order.alcohol == None:
                    full_order = dict(order.foods, **order.alcohol_free)
                if order.alcohol_free == None:
                    full_order = dict(order.foods, **order.alcohol)
                if order.alcohol_free and order.alcohol == None:
                    full_order = dict(order.foods)
                self.calculate_order_cost(name, surname)
                self.calculate_prep_time(name, surname)
                print(f"Total cost is {self.get_order_cost(name, surname)} dollars")
                print("Your order is :")
                for key, value in full_order.items():
                    print(f"{key}, quantity: {value}")
                print(f"Total preparation time will be around {order.prep_time} mins")

    def get_order_cost(self, name: str, surname: str) -> Union[int, float]:
        for order in self.orders:
            if order.name == name and order.surname == surname:
                return order.total_cost

    def calculate_prep_time(self, name: str, surname: str) -> None:
        menu = Menu().get_menu()
        for order in self.orders:
            if order.name == name and order.surname == surname:
                for key, value in order.foods.items():
                    order.prep_time += (
                        int(menu[key]["prep.time"].replace("min", "")) * value
                    )
                if order.alcohol == None:
                    pass
                else:
                    for key, value in order.alcohol.items():
                        order.prep_time += (
                            int(menu[key]["prep.time"].replace("min", "")) * value
                        )
                if order.alcohol_free == None:
                    pass
                else:
                    for key, value in order.alcohol_free.items():
                        order.prep_time += (
                            int(menu[key]["prep.time"].replace("min", "")) * value
                        )