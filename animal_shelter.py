from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username, password, host2, port3):
        # Hard-wired connection to the AAC database and animals collection
        #USER = 'aacuser'
        #PASS = 'over9000'
        #HOST = 'nv-desktop-services.apporto.com'
        #PORT = 30238
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize Connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username,password,host2,port3))
        self.database = self.client[DB]
        self.collection = self.database[COL]

#Create a new Document
#data: Document to be inserted
    def create(self, data):

        if data is not None:
            try:
                self.collection.insert_one(data)  # Insert the document
                return True
            except Exception as e:
                print(f"Error inserting document: {e}")
        else:
            print("Nothing to save, because data parameter is empty")
        return False

#Quering documents from the specific collection and returning the list of documents if successful or empty if not
#query: parameters to search documents
    def read(self, query):

        if query is not None:
            try:
                cursor = self.collection.find(query)
                results = list(cursor)
                return results
            except Exception as e:
                print(f"Error retrieving documents: {e}")
                return []
        else:
            print("Query is empty")
            return []
#Update documents in a specified database and collection. 
#query: parameters to search documents
#updated_values: new values used for update
    def update(self, query, update_values):
        if query is not None and update_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": update_values})
                return result.modified_count
            except Exception as e:
                print(f"Error updating documents: {e}")
                return 0
        else:
            print("Query or new values are empty")
            return 0
#Delete documents from the collection
#query: parameters to search the documents
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print(f"Error deleting documents: {e}")
                return 0
        else:
            print("Query is empty")
            return 0