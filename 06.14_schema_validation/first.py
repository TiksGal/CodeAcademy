from pymongo import MongoClient
from pymongo.errors import OperationFailure

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Define the schema validation rules
validation_rules = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['name', 'age', 'is_student', 'address', 'birth_date', 'metadata', 'favorite_things'],
        'properties': {
            'name': {
                'bsonType': 'string',
                'description': 'Name must be a string.'
            },
            'age': {
                'bsonType': 'int',
                'minimum': 0,
                'maximum': 120,
                'description': 'Age must be an integer between 0 and 120.'
            },
            'is_student': {
                'bsonType': 'bool',
                'description': 'is_student must be a boolean value.'
            },
            'address': {
                'bsonType': 'object',
                'required': ['street', 'city', 'country'],
                'properties': {
                    'street': {
                        'bsonType': 'string',
                        'description': 'Street must be a string.'
                    },
                    'city': {
                        'bsonType': 'string',
                        'description': 'City must be a string.'
                    },
                    'country': {
                        'bsonType': 'object',
                        'required': ['name', 'code'],
                        'properties': {
                            'name': {
                                'bsonType': 'string',
                                'description': 'Country name must be a string.'
                            },
                            'code': {
                                'bsonType': 'string',
                                'description': 'Country code must be a string.'
                            }
                        }
                    }
                }
            },
            'birth_date': {
                'bsonType': 'string',
                'pattern': '^\d{4}-\d{2}-\d{2}$',
                'description': 'Birth date must be in the format YYYY-MM-DD.'
            },
            'metadata': {
                'bsonType': 'object',
                'required': ['category', 'priority'],
                'properties': {
                    'category': {
                        'bsonType': 'string',
                        'description': 'Category must be a string.'
                    },
                    'priority': {
                        'bsonType': 'int',
                        'description': 'Priority must be an integer.'
                    }
                }
            },
            'favorite_things': {
                'bsonType': 'array',
                'items': {
                    'enum': ['apple', 5, False]
                },
                'description': 'Favorite things must be an array containing "apple", 5, and False.'
            }
        }
    }
}

# Set the validation rules for the collection
try:
    db.command('collMod', collection.name, validator=validation_rules)
    print("Schema validation enabled.")
except OperationFailure as e:
    print(f"Failed to enable schema validation: {e.details['errmsg']}")

# Example document
document = {
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
    "metadata": {
        "category": "A",
        "priority": 1
    },
    "favorite_things": ["apple", 5, False]
}

# Insert the document
collection.insert_one(document)

# Retrieve all documents from the collection
documents = collection.find()
for doc in documents:
    print(doc)

# # Clean up (optional)
# collection.drop()

