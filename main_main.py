import uuid
import firebase_admin
from firebase_admin import credentials, firestore

# connecting to firebase.
key = r"C:\Users\punee\Downloads\login-lakshh-firebase-adminsdk-hu91e-5712af1dcf.json"
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)
db = firestore.client()

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
    
    @staticmethod
    def check_document_existence(collection, document):

        doc_ref = db.collection(collection).document(document)
        doc = doc_ref.get()
        if doc.exists:
            return True
        else:
            return False
        
    @staticmethod
    def check_documents_field(collection, document, field, value):

        doc_ref = db.collection(collection).document(document)
        doc = doc_ref.get()
        dict = doc.to_dict()
        
        if dict[field] == value:
            return True
        
        else:
            return False
        
    @staticmethod
    def check_field_each_doc(collection, field, value):
        
        docs = db.collection(collection).stream()

        for doc in docs:
            doc_data = doc.to_dict()
            doc_id = doc.id

            if doc_data[field] == value:
                return doc_data

        return False
    

class User:

    def __init__(self, email):

        self.email = email

        print("Catelog : ")
        print("\t1      Spectate the Requests")
        print("\t2      Issue a Request")

        choice = int(input("Enter your choice according to catelog : "))
        
        while True:

            if choice == 1:
                self.spectate_request()
                break

            elif choice == 2:
                self.issue_request()
                break

            else:
                print("Wrong choice. TRY Again !!!")

    def spectate_request(self):

        request_dic = Firestore.check_field_each_doc("requests", "email", self.email)
        
        if request_dic == False:
            print("you have issued no request !!")

        else:

            list_fields = ["name", "course", "email", "gmane", "status"]
            print(f"game : {request_dic["game"]}")
            
            for i in request_dic:
                if i not in list_fields:
                    print(f"\t{i}:  {request_dic[i]}")
            
    def issue_request(self):

        inv_dict = Firestore.read_collection("inv")
        user_info_dict = Firestore.read_document("userRole  ",self.email)

        count  = 1
        print("CATALOG : ")
        for i in inv_dict:
            print(f"\t{count} -----> {i}")
            count += 1
        while True:
            game_choice = int(input("Enter any game of choice : "))
            request_dict = {}
            if 1 <= game_choice <= count - 1:
                game = list(inv_dict.keys())[game_choice - 1]          
                print(f"game choosed -----> {game}")
                for j in inv_dict[game]:
                    while True:    
                        temp = int(input(f"quant of {j} : "))
                        if temp > inv_dict[game][j]:
                            print("OUT OF STOCK. TRY Again !!!")
                        else:
                            request_dict[j] = temp
                            break
                
                request_dict["name"] = user_info_dict["name"]
                request_dict["email"] = user_info_dict["eail"]
                request_dict["game"] = user_info_dict["game"]
                request_dict["status"] = "pending"
                request_dict["course"] = user_info_dict["course"]
                Firestore.write_document("requests", str(uuid.uuid4()), request_dict)
                break           
            else:
                print("wrong choice. TRY Again !!")
        