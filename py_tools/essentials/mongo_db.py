from pymongo import MongoClient
try:
    from .env_to_var import env_to_var
except ImportError:
    from env_to_var import env_to_var

class MongoDBHandler:
    def __init__(self, uri=env_to_var("MONGO_URI"), db_name="ClearCanvas"):
        """Initialize the MongoDB connection."""
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_document(self, collection_name, document):
        """Insert a document into a collection."""
        collection = self.db[collection_name]
        return collection.insert_one(document)

    def find_document(self, collection_name, query):
        """Find a single document based on a query."""
        collection = self.db[collection_name]
        return collection.find_one(query)

    def find_documents(self, collection_name, query):
        """Find multiple documents based on a query."""
        collection = self.db[collection_name]
        return collection.find(query)

    def update_document(self, collection_name, query, new_values):
        """Update a single document."""
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': new_values})

    def delete_document(self, collection_name, query):
        """Delete a single document based on a query."""
        collection = self.db[collection_name]
        return collection.delete_one(query)
    
    def delete_documents(self, collection_name, query):
        """Delete multiple documents based on a query."""
        collection = self.db[collection_name]
        return collection.delete_many(query)
    
    def print_all_documents(self):
        """Print all documents from all collections in the database."""
        collections = self.db.list_collection_names()
        for collection_name in collections:
            collection = self.db[collection_name]
            documents = collection.find()
            print(f"Collection: {collection_name}")
            for document in documents:
                print(document)
            print("\n")

    def close_connection(self):
        """Close the MongoDB connection."""
        self.client.close()

def main() -> None:
    mongo = MongoDBHandler()
    
    mongo.delete_documents("users", {})
    
if __name__ == '__main__':
    main()