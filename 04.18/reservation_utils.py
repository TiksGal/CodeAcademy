from typing import Union
from datetime import datetime

current_time = datetime.now().strftime("%H:%M")


def is_reservation_made() -> str:
    while True:
        user_answer = input("Have you made a reservation?(Yes/No): ").strip().lower()
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def handle_new_reservation() -> str:
    while True:
        user_answer = (
            input("Do you want to make a new reservation?(Yes/No): ").strip().lower()
        )
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def is_going_to_eat_now() -> str:
    while True:
        user_answer = input("Are you going to eat now?(Yes/No): ").strip().lower()
        if user_answer != "yes" and user_answer != "no":
            print("You must type yes or no")
            continue
        else:
            return user_answer


def get_valid_table_id() -> int:
    while True:
        try:
            table_id = int(input("And the id of the table type?: ").strip())
            return table_id
        except ValueError:
            print("You must enter valid number")
            continue


def get_valid_table_type() -> str:
    while True:
        valid_table_types = ["single", "double", "family"]
        table_type = (
            input("What table would you like to reserve?(single,double,family): ")
            .strip()
            .lower()
        )
        if table_type not in valid_table_types:
            print("This table type does not exist! Choose a valid one")
            continue
        else:
            return table_type


def get_valid_time() -> str:
    while True:
        time = input("At what time would you like to reserve?(format hh:mm): ").strip()
        if ":" not in time:
            print("Wrong time format! Must be hh:mm")
            continue
        else:
            return time


def identify_input(user_input: str) -> bool:
    if user_input == "yes":
        return True
    if user_input == "no":
        return False


def get_reservation_info() -> Union[str, int]:
    name = input("Please tell us your name: ").strip()
    surname = input("And surname: ").strip()
    table_type = get_valid_table_type()
    table_id = get_valid_table_id()
    user_answer = is_going_to_eat_now()
    if identify_input(user_answer):
        time = current_time
    else:
        time = get_valid_time()

    return name, surname, table_type, table_id, time