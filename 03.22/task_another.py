import re
from dotenv import dotenv_values

config = dotenv_values(".env")


def parse_encoded_string():
    encoded_string = config["encoded_string"]
    parts = re.split('0+', encoded_string)
    # Extract the first name, last name, and id from the parts list
    first_name = parts[0]
    last_name = parts[1]
    id = ''.join(parts[2:])  # Concatenate all remaining parts into a single string

    # Create a dictionary containing the parsed values
    parsed_dict = {
        'first_name': first_name,
        'last_name': last_name,
        'id': id
    }

    return parsed_dict


parsed_dict = parse_encoded_string()
print(parsed_dict)

