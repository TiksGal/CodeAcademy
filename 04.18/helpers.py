import json


def identify_input(user_input: str) -> bool:
    if user_input == "yes":
        return True
    if user_input == "no":
        return False


def print_menu(submenu_name: str) -> str:
    print(
        f'{json.dumps(submenu_name, indent=2).replace("{", "").replace("}", "").strip()}'
    )


def is_value_not_none(variable_name) -> bool:
    if variable_name == None:
        return False
    return True