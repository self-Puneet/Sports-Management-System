from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore

key = "C:\Users\punee\Downloads\sports-management-database-firebase-adminsdk-j2q72-a620bd1e37.json"
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)
db = firestore.client()

class Login:

    def __init__(self):

        reply = input ("\tWelcome !! are you registered (Y/N) : " )

        if reply == "y" or "Y":
            self.login()

        elif reply == "N" or "n":
            self.signup()

    def login(self):

        email_flag = 1
        password_flag = 1
        
        while email_flag == password_flag == 1:
            
            if email_flag == 1:
                email = input("Enter your SPSU e-mail id : ")
            
            if password_flag == 1:
                password = input("Enter your password : ")
            
            return_value = self.credential_check (email, password) 
            
            if return_value == -1:
                print(f"No record of {email} in our database")

            elif return_value == 0:
                print("password is wrong. Try Again !!")
                email_flag = 0

            else:
                print(f"Hi {return_value} !!")
                email_flag = password_flag = 0

    def signup(self):

        while True: 
            
            email = input("Enter your SPSU email id : ")
            if self.credential_check((email)):
                break
            
        while True:

            password = input("Set suitable password : ")
            temp = input("Comfirm the above password : ")
            
            if temp == password :

                doc_ref = db.collection('credentials').document('signup_database')
                doc = doc_ref.get()
                data = doc.to_dict()[email]
                data[0] = password
                doc_ref.update({email:data})

                break

            else:
                print("comfirmation failed. TRY Again !!")

    def credential_check(self, cred_tuple):

        if len(cred_tuple) == 2:

            doc_ref = db.collection('credentials').document('signup_database')
            doc = doc_ref.get()
            data = doc.to_dict()
            
            email, password = cred_tuple[0], cred_tuple[1]
    
            if email in data.keys():
                if data[email][0] == password:
                    return data[email][1]
                else:
                    return 0
            else:
                return -1
        
        else:
            
            doc_ref = db.collection('credentials').document('SPSU_database')
            doc = doc_ref.get()
            data = doc.to_dict()

            email = cred_tuple[0]
            if email in data.keys():
                return True
            else:
                return False
            

class Request:
    email = None
    equipment_dict = None
    equipment_lim = None
    time_lim = None
    
    def __init(self, e_mail):
        email = e_mail

        doc_ref = db.collection('admin_perms').document('game_database')
        doc = doc_ref.get()
        self.equipment_dict = doc.to_dict()

        doc_ref = db.collection('admin_perms').document('equipments_limitation_database')
        self.equipment_lim = doc.to_dict()

        doc_ref = db.collection('admin_perms').document('time_limitation_database')
        self.time_lim = doc.to_dict()
        
        self.game_choice()

    def game_choice(self):
        
        for i in range(1, len(self.equipment_dict) + 1):
            print(f"\t{i}\t\t{list(self.equipment_dict.keys())[i-1]}")

        while True:

            game_id = int(input("Enter your choice from above catalogue: "))
            
            if 1 <= game_id <= len(self.equipment_dict):
                game = list(self.equipment_dict.keys())[game_id]
                self.handle_request(game, game_id)

            else:
                print("You have choosen wrond game id. TRY again !!") 

    def handle_request(self, game, game_id):

        print("Give quantity of each item:")
        quantity = []

        for i in range(0, len(self.equipment_dict[game])):
            
            while True:

                quantity = int(input(f"\t{self.equipment_dict[game][i]} : "))
                
                if quantity > self.equipment_lim[game][i][1]:
                    print(f"out of stock. TRY again later or reduce quantity.")
                
                else:            
                    if quantity > self.equipment_lim[game][i][0]:
                        print(f"maximum issueable {self.equipment_dict[game][i]} at a time are {self.equipment_lim[game][i][0]}. TRY Again !!")
                    else:
                        quantity.append(quantity)
                        break
        
        time = input("Time duration for issue : ")
        
        while True:
                 
            if time > self.time_lim[game]:
                print(f"issueing time could not exceed {self.time_lim[game]}. TRY again !!")
                time = input("Time duration for issue : ")

            else:
                break

        self.writting_request ([game_id, quantity], time)
    
    def writting_request(self, request_id, time):

        status = 'pending'
        doc_ref = db.collection('request').document('request')
        doc = doc_ref.get()
        data = {self.email : [request_id, status, time]}
        doc_ref.update(data)

        print("request is send to our server successfully !!")

        
