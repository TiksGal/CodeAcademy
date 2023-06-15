import menu as menu


def check_if_food_valid(food_name: str) -> bool:
    if food_name not in menu.VALID_FOODS:
        return False
    return True


def check_if_drink_valid(drink_name: str) -> bool:
    if drink_name not in menu.VALID_DRINKS:
        if drink_name not in menu.VALID_ALC_DRINKS:
            return False
        return True
    return True


def get_valid_meal_order() -> str:
    while True:
        food = (
            input("What meal would you like to order?(Type one name at the time): ")
            .strip()
            .capitalize()
        )
        if check_if_food_valid(food):
            return food
        else:
            continue


def get_valid_meal_quantity() -> int:
    while True:
        try:
            quantity = int(input("How many of said meal?(Type a number): ").strip())
            return quantity
        except ValueError:
            print("Input must be an integer")
            continue


def handle_extra_meal_order() -> str:
    while True:
        user_answer = (
            input("Do you want to order anything else from food the menu?(Yes/No): ")
            .strip()
            .lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def handle_drink_orders() -> str:
    while True:
        user_answer = (
            input("Do you want to order any drinks?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
        else:
            return user_answer


def get_valid_drink_order() -> str:
    while True:
        drink = (
            input("What drink would you like to order?(Type one name at the time): ")
            .strip()
            .capitalize()
        )
        if check_if_drink_valid(drink):
            return drink
        else:
            continue


def get_valid_drink_quantity() -> int:
    while True:
        try:
            quantity = int(
                input("And how many of said drink?(Type a number): ").strip()
            )
            return quantity
        except ValueError:
            print("Input must be an integer")
            continue


def handle_extra_drink_order() -> str:
    while True:
        user_answer = (
            input("Do you want to order anything else from drinks menu?(Yes/No): ")
            .strip()
            .lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def handle_order_now() -> str:
    while True:
        user_answer = (
            input("Do you want to make an order right now?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def is_ready_to_order() -> str:
    while True:
        user_answer = (
            input("Tell us when you will be ready to order(Type: ready): ")
            .strip()
            .lower()
        )
        if user_answer != "ready":
            print("You must type word 'ready' when you are ready to order")
        else:
            break