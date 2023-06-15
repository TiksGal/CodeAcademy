from pymongo import MongoClient


def check_data(collection, field_name, equal_value, not_equal_value):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["testas111"]

    # Check if the database exists
    db_list = client.list_database_names()
    if "testukas111" in db_list:
        print("The database exists.")
    else:
        print("The database does not exist.")

    collection = db[collection]

    # Check if the collection exists
    collection_list = db.list_collection_names()
    if "testas1" in collection_list:
        print("The collection exists.")
    else:
        print("The collection does not exist.")

    documents = collection.find({field_name: {"$eq": equal_value, "$ne": not_equal_value}})

    docs = list(documents)
    if docs:
        print("Documents found: ", docs)
    else:
        print("No documents found.")

    return docs


docs = check_data("testas1", "Name", "elix", "lenix")
