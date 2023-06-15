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
        'required': ['person', 'products'],
        'properties': {
            'person': {
                'bsonType': 'object',
                'required': ['name', 'age', 'is_student', 'address', 'contacts', 'education'],
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
                    'contacts': {
                        'bsonType': 'array',
                        'items': {
                            'bsonType': 'object',
                            'required': ['type', 'value'],
                            'properties': {
                                'type': {
                                    'bsonType': 'string',
                                    'description': 'Contact type must be a string.'
                                },
                                'value': {
                                    'bsonType': 'string',
                                    'description': 'Contact value must be a string.'
                                }
                            }
                        }
                    },
                    'education': {
                        'bsonType': 'array',
                        'items': {
                            'bsonType': 'object',
                            'required': ['institution', 'degree', 'major', 'completed'],
                            'properties': {
                                'institution': {
                                    'bsonType': 'string',
                                    'description': 'Institution must be a string.'
                                },
                                'degree': {
                                    'bsonType': 'string',
                                    'description': 'Degree must be a string.'
                                },
                                'major': {
                                    'bsonType': 'string',
                                    'description': 'Major must be a string.'
                                },
                                'completed': {
                                    'bsonType': 'bool',
                                    'description': 'Completed must be a boolean value.'
                                }
                            }
                        }
                    }
                }
            },
            'products': {
                'bsonType': 'array',
                'items': {
                    'bsonType': 'object',
                    'required': ['id', 'name', 'price', 'is_available'],
                    'properties': {
                        'id': {
                            'bsonType': 'int',
                            'description': 'ID must be an integer.'
                        },
                        'name': {
                            'bsonType': 'string',
                            'description': 'Product name must be a string.'
                        },
                        'price': {
                            'bsonType': 'double',
                            'description': 'Price must be a double.'
                        },
                        'is_available': {
                            'bsonType': 'bool',
                            'description': 'Availability must be a boolean value.'
                        }
                    }
                }
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
json_object = {
    "person": {
        "name": "John Doe",
        "age": 30,
        "is_student": False,
        "address": {
            "street": "456 Elm Street",
            "city": "San Francisco",
            "country": {
                "name": "United States",
                "code": "US"
            }
        },
        "contacts": [
            {
                "type": "email",
                "value": "john.doe@example.com"
            },
            {
                "type": "phone",
                "value": "1 123-456-7890"
            }
        ],
        "education": [
            {
                "institution": "University of XYZ",
                "degree": "Bachelor's",
                "major": "Computer Science",
                "completed": True
            },
            {
                "institution": "ABC College",
                "degree": "Master's",
                "major": "Data Science",
                "completed": False
            }
        ]
    },
    "products": [
        {
            "id": 1,
            "name": "Product 1",
            "price": 19.99,
            "is_available": True
        },
        {
            "id": 2,
            "name": "Product 2",
            "price": 29.99,
            "is_available": False
        }
    ]
}

# Insert the document
collection.insert_one(json_object)

# Retrieve all documents from the collection
documents = collection.find()
for doc in documents:
    print(doc)

# # Clean up (optional)
# collection.drop()
