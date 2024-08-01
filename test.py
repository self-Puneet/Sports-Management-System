# import firebase_admin
# from firebase_admin import credentials, firestore

# key = r"C:\Users\punee\Downloads\sports-management-database-firebase-adminsdk-j2q72-a620bd1e37.json"
# cred = credentials.Certificate(key)

# # Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred)

# # Initialize Firestore DB
# db = firestore.client()

# # Reference to the collection
# collection_name = 'userRoles'

# # Get all documents in the collection
# docs = db.collection(collection_name).stream()
# print(type(docs))
# # Iterate through the documents and print their data
# doc_data = {}

# # Iterate through the documents and append their data to the dictionary
# for doc in docs:
#     doc_data[doc.id] = doc.to_dict()

# # Print the dictionary with all document data
# print(doc_data)



class Firestore:

    @staticmethod
    def printh(string):
        print(string)

Firestore.printh("hello")