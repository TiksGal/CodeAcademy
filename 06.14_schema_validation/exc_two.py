from pymongo import MongoClient, errors

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create a new database
db = client['shopping_db']

# Define the schema validation rules
validation_rules = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['name', 'age', 'email', 'address'],
        'properties': {
            'name': {
                'bsonType': 'string',
                'description': 'must be a string'
            },
            'age': {
                'bsonType': 'int',
                'minimum': 18,
                'maximum': 99,
                'description': 'must be an integer in [18, 99]'
            },
            'email': {
                'bsonType': 'string',
                'pattern': '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$',
                'description': 'must be a string and match the regular expression pattern'
            },
            'address': {
                'bsonType': 'object',
                'required': ['street', 'city', 'postal_code'],
                'properties': {
                    'street': {
                        'bsonType': 'string',
                        'description': 'must be a string'
                    },
                    'city': {
                        'bsonType': 'string',
                        'description': 'must be a string'
                    },
                    'postal_code': {
                        'bsonType': 'string',
                        'description': 'must be a string'
                    }
                }
            }
        }
    }
}

# Create collection with validation rules
try:
    db.create_collection('shopping_collection', validator=validation_rules, validationLevel='strict')
    print("Collection created with schema validation enabled.")
except errors.CollectionInvalid:
    print("Collection already exists. Modifying validator.")
    try:
        db.command('collMod', 'shopping_collection', validator=validation_rules)
        print("Schema validation enabled.")
    except errors.OperationFailure as e:
        print(f"Failed to enable schema validation: {e.details['errmsg']}")

collection = db['shopping_collection']

# Documents to insert
docs = [
    {  # valid
        "name": "John", 
        "age": 25, 
        "email": "john@example.com", 
        "address": {
            "street": "123 Main Street",
            "city": "Some City",
            "postal_code": "12345"
        }
    },
    {  # invalid (age < 18)
        "name": "Sam", 
        "age": 17, 
        "email": "sam@example.com", 
        "address": {
            "street": "456 Elm Street",
            "city": "Another City",
            "postal_code": "67890"
        }
    },
    {  # invalid (missing 'postal_code' in 'address')
        "name": "Kate", 
        "age": 25, 
        "email": "kate@example.com", 
        "address": {
            "street": "789 Oak Street",
            "city": "Third City"
        }
    }
]

# Insert the documents and handle any potential validation errors
for doc in docs:
    try:
        collection.insert_one(doc)
    except errors.WriteError as e:
        print(f"Could not insert document {doc}. Error: {str(e)}")

# Print all the documents in the collection
for doc in collection.find():
    print(doc)

# Clean up
collection.drop()
client.close()


