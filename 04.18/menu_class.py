from dataclasses import dataclass
from typing import Union, Dict, Optional, List
import menu as menu_dict
from datetime import datetime
import helpers as helpers


@dataclass
class Menu:
    current_time = int(datetime.now().strftime("%H"))
    alcohol = menu_dict.DRINKS["Alcohol"]
    alcohol_free = menu_dict.DRINKS["Alcohol free"]
    breakfast = menu_dict.BREAKFAST
    lunch = menu_dict.LUNCH
    dinner = menu_dict.DINNER
    vegan = menu_dict.SPECIAL_MENU["Vegan"]
    vegetarian = menu_dict.SPECIAL_MENU["Vegetarian"]

    def show_food_menu(self) -> Dict[str, Union[float, int]]:
        helpers.print_menu(submenu_name=self.vegetarian)
        helpers.print_menu(submenu_name=self.vegan)

        if 12 < self.current_time < 18:
            helpers.print_menu(submenu_name=self.lunch)
        if 12 > self.current_time:
            helpers.print_menu(submenu_name=self.breakfast)
        if 18 < self.current_time:
            helpers.print_menu(submenu_name=self.dinner)

    def show_all_drinks(self) -> Dict[str, Union[float, int]]:
        helpers.print_menu(submenu_name=self.alcohol)
        helpers.print_menu(submenu_name=self.alcohol_free)

    def get_menu(self) -> Dict[str, Dict[str, Dict[str, Union[int, float, str]]]]:
        if 12 < self.current_time < 18:
            return dict(
                self.alcohol,
                **self.alcohol_free,
                **self.vegan,
                **self.vegetarian,
                **self.lunch,
            )
        if 12 > self.current_time:
            return dict(
                self.alcohol,
                **self.alcohol_free,
                **self.vegan,
                **self.vegetarian,
                **self.breakfast,
            )
        if 18 < self.current_time:
            return dict(
                self.alcohol,
                **self.alcohol_free,
                **self.vegan,
                **self.vegetarian,
                **self.dinner,
            )