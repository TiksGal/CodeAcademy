from pymongo import MongoClient, errors
from pymongo.errors import OperationFailure

# Connect to MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Create a new database and a collection
db = client['exercise_db']
collection = db['exercise_collection']

# Define the schema validation rules
validation_rules = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['name', 'age', 'email'],
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
            }
        }
    }
}

# Apply the validation rules to the collection
try:
    collection.command('collMod', collection.name, validator=validation_rules)
    print("Schema validation enabled.")
except OperationFailure as e:
    print(f"Failed to enable schema validation: {e.details['errmsg']}")

# Documents to insert
docs = [
    {"name": "John", "age": 25, "email": "john@example.com"},  # valid
    {"name": "Sam", "age": 17, "email": "sam@example.com"},  # invalid (age < 18)
    {"name": "Kate", "age": 25, "email": "kate"}  # invalid (email not valid)
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

