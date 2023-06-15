import json

json_object = {
    "name": "John Doe",
    "age": 25,
    "is_student": True,
    "interests": ["reading", "traveling", "photography"],
    "address": {
        "street": "123 Main Street",
        "city": "New York",
        "country": {
            "name": "United States",
            "code": "US"
        }
    },
    "birth_date": "1998-05-10",
    "metadata": {"category": "A", "priority": 1},
    "favorite_things": ["apple", 5, False]
}

# Save the json_object to a file
with open('json_object.json', 'w') as file:
    json.dump(json_object, file)
