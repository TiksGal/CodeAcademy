from menu_class import Menu
from orders_classes import Order, Orders
from tables_class import Reservation, Tables
import helpers as helpers
from datetime import datetime
import menu as menu_dicts
import reservation_utils as res_utils
import ordering_utils as ord_utils

menu = Menu()
tables = Tables()
orders = Orders()

current_time = datetime.now().strftime("%H:%M")

print("Welcome to our cafetera!")
user_answer = res_utils.is_reservation_made()

if helpers.identify_input(user_answer):
    print(
        "We are sorry, but we have no reservations yet, there must have been an error"
    )
    user_answer = res_utils.handle_new_reservation()
    if helpers.identify_input(user_answer):
        print("Here are our free tables at the moment:")
        print("Choose the table you want from the free tables list:")
        tables.show_free_tables()
        print("We will need some information to make a new reservation")
        (
            name,
            surname,
            table_type,
            table_id,
            time,
        ) = res_utils.get_reservation_info()
        tables.reserve_table(
            name=name,
            surname=surname,
            table_type=table_type,
            table_id=table_id,
            time=time,
        )
        print(tables.show_reservation(name=name, surname=surname))
    else:
        print("Have a nice day then!")

else:
    user_answer = res_utils.handle_new_reservation()
    if helpers.identify_input(user_answer):
        print("Here are our free tables at the moment:")
        print("Choose the table you want from the free tables list:")
        tables.show_free_tables()
        print("We will need some information to make a new reservation")
        (
            name,
            surname,
            table_type,
            table_id,
            time,
        ) = res_utils.get_reservation_info()
        tables.reserve_table(
            name=name,
            surname=surname,
            table_type=table_type,
            table_id=table_id,
            time=time,
        )
        print(tables.show_reservation(name=name, surname=surname))

    else:
        print("Have a nice day then!")


user_answer = ord_utils.handle_order_now()

if helpers.identify_input(user_answer):
    print("Here is our food menu:")
    menu.show_food_menu()
    foods = {}
    while True:
        food = ord_utils.get_valid_meal_order()
        quantity = ord_utils.get_valid_meal_quantity()
        foods[food] = quantity
        user_answer = ord_utils.handle_extra_meal_order()
        if user_answer == "no":
            break
        else:
            continue

    user_answer = ord_utils.handle_drink_orders()
    if helpers.identify_input(user_answer):
        print("Here is our drinks menu: ")
        menu.show_all_drinks()
        alcohol = {}
        alc_free = {}
        while True:
            drink = ord_utils.get_valid_drink_order()
            quantity = ord_utils.get_valid_drink_quantity()
            if drink in menu_dicts.VALID_ALC_DRINKS:
                alcohol[drink] = quantity
            else:
                alc_free[drink] = quantity

            user_answer = ord_utils.handle_extra_drink_order()
            if user_answer == "no":
                break
            else:
                continue
        if alcohol:
            pass
        else:
            alcohol = None
        if alc_free:
            pass
        else:
            alc_free = None

        orders.make_order(
            name=name,
            surname=surname,
            foods=foods,
            alcohol=alcohol,
            alcohol_free=alc_free,
        )

        orders.show_order_summarized(name=name, surname=surname)
    else:
        alcohol = None
        alc_free = None
        orders.make_order(
            name=name,
            surname=surname,
            foods=foods,
            alcohol=alcohol,
            alcohol_free=alc_free,
        )
        orders.show_order_summarized(name=name, surname=surname)
else:
    ord_utils.is_ready_to_order()
    print("Here is our food menu:")
    menu.show_food_menu()
    foods = {}
    while True:
        food = ord_utils.get_valid_meal_order()
        quantity = ord_utils.get_valid_meal_quantity()
        foods[food] = quantity
        user_answer = ord_utils.handle_extra_meal_order()
        if user_answer == "no":
            break
        else:
            continue

    user_answer = ord_utils.handle_drink_orders()
    if helpers.identify_input(user_answer):
        print("Here is our drinks menu: ")
        menu.show_all_drinks()
        alcohol = {}
        alc_free = {}
        while True:
            drink = ord_utils.get_valid_drink_order()
            quantity = ord_utils.get_valid_drink_quantity()
            if drink in menu_dicts.VALID_ALC_DRINKS:
                alcohol[drink] = quantity
            else:
                alc_free[drink] = quantity

            user_answer = ord_utils.handle_extra_drink_order()
            if user_answer == "no":
                break
            else:
                continue
        if alcohol:
            pass
        else:
            alcohol = None
        if alc_free:
            pass
        else:
            alc_free = None

        orders.make_order(
            name=name,
            surname=surname,
            foods=foods,
            alcohol=alcohol,
            alcohol_free=alc_free,
        )

        orders.show_order_summarized(name=name, surname=surname)
    else:
        alcohol = None
        alc_free = None
        orders.make_order(
            name=name,
            surname=surname,
            foods=foods,
            alcohol=alcohol,
            alcohol_free=alc_free,
        )
        orders.show_order_summarized(name=name, surname=surname)