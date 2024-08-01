# necessery libraries
import uuid
import re

import firebase_admin
from firebase_admin import credentials, firestore

# connecting to firebase.
key = r"C:\Users\punee\Downloads\sports-management-database-firebase-adminsdk-j2q72-a620bd1e37.json"
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)
db = firestore.client()

# =============================== class for reading and writting in firestore database =============================

class Firestore:

    # for reading the conetent of specified document under a  given collection
    @staticmethod
    def read_document(collection, document) -> dict:
        
        doc_ref = db.collection(collection).document(document)
        doc = doc_ref.get()
        return doc.to_dict()

    # writting into specified document with specified collection
    
    @staticmethod
    def write_document(collection, document, data) -> None:
        
        doc_ref = db.collection(collection).document(document)
        doc_ref.set(data, merge = True)

    # reading the content of all the documents in a specified collection
    
    @staticmethod
    def read_collection(collection) -> dict:
        
        docs = db.collection(collection).stream()
        doc_data = {}
        for doc in docs:
            doc_data[doc.id] = doc.to_dict()
        
        return doc_data

# ======================================= class for SignUP and login of user ====================================

class SignUp:

    # for signup of first user appearence
    
    def signup(self):

        email = input("Enter your SPSU email id : ")
        erp_data_dict = Firestore.read_document("preErp", "phone_no")
        
        # if provided email is in erp database
        if email in erp_data_dict.keys():

            phone_no = erp_data_dict[email]
            temp = re.search(r"^(.*?)@", email).group(1)
            name, temp = temp.split(".")
            course = re.search(r"^(.*?)(?=\d)", temp).group(1)        
            
            data = {
                "email" : email,
                "name" : name,
                "course" : course,
                "phone_no" : int(phone_no),
                "role" : "user"
            }

            Firestore.write_document("userRoles", str(uuid.uuid4()), data)

        # if provided email is not present in erp
        else:
            pass

    # for login of already registered user

    def login(self):

        while True:
            email = input("Enter your SPSU email id : ")
            userRoles_dict = Firestore.read_collection("userRoles")

            for i in userRoles_dict.keys():
                if email == userRoles_dict[i]["email"]:
                    return userRoles_dict[i]
                
            print("Wrong Email. TRY Again !!")
    
# ======================================= class for user realated functionality ====================================

class User:

    def __init__(self, email):

        print("1        Check status of request")
        print("2        Send a Request")

        choice = int(input("Enter "))

        if choice == 1:
            self.check_request()

        elif choice == 2:
            self.request()

    def check_request(self):

        pass

    def request(self):


        pass


if __name__ == "__main__":
    Obj = SignUp()
    Obj.signup()