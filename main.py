import uuid

import firebase_admin
from firebase_admin import credentials, firestore

key = r"C:\Users\punee\Downloads\sports-management-database-firebase-adminsdk-j2q72-a620bd1e37.json"
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)
db = firestore.client()

def read_document():
    # read the document's fields and returns document in form of dictionary
    pass

def write_document():
    # takes input in form of dict and writes the content into document
    pass

class SignUp:

    def signup(self):

        email = input("Enter your SPSU email id : ")
        erp_data_dict = read_document("preErp", "phone_no")
        
        if email in erp_data_dict.keys():

