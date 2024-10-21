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

    def insert_document(self, collection_name: str, document: dict) -> None:
        """Insert a document into a collection."""
        collection = self.db[collection_name]
        return collection.insert_one(document)

    def find_document(self, collection_name: str, query: dict) -> dict:
        """Find a single document based on a query."""
        collection = self.db[collection_name]
        return collection.find_one(query)

    def find_documents(self, collection_name: str, query: dict) -> list:
        """Find multiple documents based on a query."""
        collection = self.db[collection_name]
        return collection.find(query)

    def update_document(self, collection_name: str, query: dict, new_values: dict):
        """Update a single document."""
        collection = self.db[collection_name]
        return collection.update_one(query, {'$set': new_values})

    def delete_document(self, collection_name: str, query: dict) -> None:
        """Delete a single document based on a query."""
        collection = self.db[collection_name]
        return collection.delete_one(query)
    
    def delete_documents(self, collection_name: str, query: dict) -> None:
        """Delete multiple documents based on a query."""
        collection = self.db[collection_name]
        return collection.delete_many(query)
    
    def print_all_documents(self) -> None:
        """Print all documents from all collections in the database."""
        collections = self.db.list_collection_names()
        for collection_name in collections:
            collection = self.db[collection_name]
            documents = collection.find()
            print(f"Collection: {collection_name}")
            for document in documents:
                print(document)
            print("\n")

    def close_connection(self) -> None:
        """Close the MongoDB connection."""
        self.client.close()

def main() -> None:
    mongo = MongoDBHandler()
    
    # mongo.delete_documents("coordinates", {})
    # mongo.update_document("users", {"username": "ved-patel226"}, {"role": "teacher"})
    mongo.insert_document("users", {"username": "ved-patel226", "role": "student"})
    mongo.print_all_documents()
        
        
if __name__ == '__main__':
    main()