from datetime import datetime
import re

import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import DELETE_FIELD

key = r"C:\Users\punee\Downloads\sports-management-database-firebase-adminsdk-j2q72-a620bd1e37.json"
cred = credentials.Certificate(key)
firebase_admin.initialize_app(cred)
db = firestore.client()

class Login:

    def __init__(self):

        reply = input("\tWelcome !! are you registered (Y/N) : " )

        if reply == "N" or reply == "n":            
            self.signup()

        elif reply == "Y" or reply == "y":
            self.login()

    def login(self):

        email_flag = 1
        password_flag = 1
        
        while email_flag == 1 or password_flag == 1:
            
            if email_flag == 1:
                email = input("Enter your SPSU e-mail id : ")
                email_ = re.match(r"(.+?)@", email).group(1)

            if password_flag == 1:
                password = input("Enter your password : ")
            
            return_value = self.credential_check ((email_, password)) 
            
            if re.search(r"@spsu.ac.in$", email):
                if return_value == -1:
                    print(f"No record of {email} in our database")

                elif return_value == 0:
                    print("password is wrong. Try Again !!")
                    email_flag = 0

                else:
                    print(f"Hi {return_value} !!")
                    email_flag = password_flag = 0

            else:
                print(f"No record of {email} in our database")

    def signup(self):

        while True: 
            
            email = input("Enter your SPSU email id : ")
            email_ = re.match(r"(.+?)@", email).group(1)
            
            if re.search(r"@spsu.ac.in$", email) and self.credential_check(email_):
                break
            else:
                print(f"no record of {email} in our database. TRY again !!")
            
        while True:

            password = input("Set suitable password : ")
            temp = input("Comfirm the above password : ")
            
            if temp == password :

                doc_ref = db.collection('credentials').document('SPSU_database')
                doc = doc_ref.get()
                data = list(doc.to_dict()[email_])
                data.append(password)

                doc_ref = db.collection('credentials').document('signup_database')
                doc_ref.set({str(email_): data}, merge = True)

                break

            else:
                print("comfirmation failed. TRY Again !!")

    def credential_check(self, cred_tuple):

        if len(cred_tuple) == 2:

            doc_ref = db.collection('credentials').document('signup_database')
            doc = doc_ref.get()
            data = doc.to_dict()
            
            email_, password = cred_tuple[0], cred_tuple[1]
    
            if email_ in data.keys():
                if data[email_][2] == password:
                    return data[email_][0]
                else:
                    return 0
            else:
                return -1
        
        else:
            email_ = cred_tuple
            
            doc_ref = db.collection('credentials').document('SPSU_database')
            doc = doc_ref.get()
            data = doc.to_dict()
            
            if email_ in data:
                return True
            else:
                return False
            
           
class User:
    
    def __init__(self, e_mail):
        self.email = e_mail

        doc_ref = db.collection('admin_perms').document('game_database')
        doc = doc_ref.get()
        self.equipment_dict = doc.to_dict()

        doc_ref = db.collection('admin_perms').document('equipments_issueing_limitation_database')
        doc = doc_ref.get()
        self.equipment_issue_lim = doc.to_dict()

        doc_ref = db.collection('admin_perms').document('equipments_limitation_database')
        doc = doc_ref.get()
        self.equipment_lim = doc.to_dict()
        
        doc_ref = db.collection('admin_perms').document('time_limitation_database')
        doc = doc_ref.get()
        self.time_lim = doc.to_dict()

        doc_ref = db.collection('request').document('request_database')
        doc = doc_ref.get()
        self.request_database = doc.to_dict()
        
        while True:

            print('''
                1   Current Request logs
                2   Request for equipments        
            ''')

            choice = int(input("choose desired option from the above catelog : "))

            if choice == 1:
                self.show_request_status()
                break
            
            elif choice == 2:
                self.game_choice()
                break
            
            else:
                print("wrong choice. TRY again !!")

    def game_choice(self):
        
        for i in range(1, len(self.equipment_dict) + 1):
            print(f"\t{i}\t\t{list(self.equipment_dict.keys())[i-1]}")

        while True:

            game_id = int(input("Enter your choice from above catalogue: "))
            
            if 1 <= game_id <= len(self.equipment_dict):
                game = list(self.equipment_dict.keys())[game_id - 1]
                self.handle_request(game, game_id - 1)

            else:
                print("You have choosen wrond game id. TRY again !!") 

    def handle_request(self, game, game_id):

        print("Give quantity of each item:")
        quantity = []

        for i in range(0, len(self.equipment_dict[game])):
            
            while True:

                quan = int(input(f"\t{self.equipment_dict[game][i]} : "))
        
                if quan > self.equipment_lim[game][i]:
                    print(f"out of stock. TRY again later or reduce quantity.")
                
                else:            
                    if quan > self.equipment_issue_lim[game][i]:
                        print(f"maximum issueable {self.equipment_dict[game][i]} at a time are {self.equipment_issue_lim[game][i]}. TRY Again !!")
                    else:
                        quantity.append(quan)
                        break
        
        quantity = ",".join(str(num) for num in quantity)
        time = int(input("Time duration for issue : "))
        
        while True:
                 
            if time > self.time_lim[game]:
                print(f"issueing time could not exceed {self.time_lim[game]}. TRY again !!")
                time = int(input("Time duration for issue : "))

            else:
                break

        self.writting_request (game_id, quantity, time)
    
    def writting_request(self, game_id, quantity, time):

        status = 'pending'
        doc_ref = db.collection('request').document('request_database')
        data = {str(self.email) : [game_id, quantity, status, time]}
        doc_ref.set(data, merge = True)

        print("request is send to our server successfully !!")

    def show_request_status(self):

        if self.email not in self.request_database.keys():
            print("No request is send by you recently ..")

        else:
            request = self.request_database[self.email]
            game = list(self.equipment_dict.keys())[request[0]]
            equipments = self.equipment_dict[game]
            quantity = [int(num) for num in request[1].split(",")]
    
            for i in range(0, len(equipments)):
                print(f"\t{equipments[i]}  :   {quantity[i]}")
            
            print(f"status   :   {request[2]}")

class Admin:

    def __init__(self, email):

        self.email = email

        doc_ref = db.collection('credentials').document('admins')
        doc = doc_ref.get()
        admin_database = doc.to_dict()
        
        self.admin = admin_database[self.email]
        
        doc_ref = db.collection('request').document('request_database')
        doc = doc_ref.get()
        self.request_database = doc.to_dict()

        doc_ref = db.collection('credenials').document('signup_database')
        doc = doc_ref.get()
        self.cred_database = doc.to_dict()

        doc_ref = db.collection('admin_perms').document('game_database')
        doc = doc_ref.get()
        self.equipment_dict = doc.to_dict()

        doc_ref = db.collection('request').document('rejected_request_databse')
        doc = doc_ref.get()
        self.rejected_req = doc.to_dict()

        print('''
            1       Adding games and equipments
            2       Spectate Requests
        ''')

    def requests(self):
        
        for i in self.request_database.keys():
            
            request = self.request_database[i]
            game = list(self.equipment_dict.keys())[request[0]]
            equipments = self.equipment_dict[game]
            quantity = [int(num) for num in request[1].split(",")]
            
            
            print(f"-----> {self.cred_database[i][0]}   ({self.cred_database[i][1]}) - {game} ")

            for j in range(0, len(equipments)):
                print(f"       -----> {equipments[j]} : {quantity[j]}")

            print("\t\t1    Accept")
            print("\t\t2    Reject")
            print("\t\t3    Spectate") 

            choice = int(input("Choose one of any option from the catelog : "))

            if choice == 3:
                None

            elif choice == 2:
                
                doc_ref = db.collection('request').document('rejected_request_database')
                self.request_database[i][2] = 'rejected'
                data = {i : self.request_database[i]}
                doc_ref.set(data, merge = True)

                doc_ref = db.collection('request').document('request_database')
                doc_ref.update({
                    i: DELETE_FIELD
                })

            elif choice == 1:
                
                doc_ref = db.collection('admin_perms').document('equipment_limit_database')
                doc_ref.update() 
                doc = doc_ref.get()
                self.request_database = doc.to_dict()
                


                self.request_database[i][2] = 'accepted'

    def  games_add_on(self):

        while True:
            
            print("1   Add games and equipments\n2   Control the issue_limit, limit, time limit\n3  exit")
            choice = int(input("choose from above catelog : "))

            if choice == 1:
                
                game = input("Enter new game : ")
                equipment = []
                temp = 'Y'
                
                while temp == 'Y' or temp == 'y':
                    equipment.append(input("Enter Equipment : "))
                    temp = input("Wanna add more equipments (Y/N) : ")

                data = {game : equipment}
                doc_ref = db.collection('admin_perms').document('game_database')
                doc_ref.update(data)

            elif choice == 2:

                doc_ref = db.collection('admin').document('game_database')
                doc = doc_ref.get()
                game_database = doc.to_dict()
                
                count = 1
                for i in game_database.keys():
                    print(f"{count} ----> {i}")

                game_choice = int(input("Enter choice from above catelog : "))
                
                print("1\Equipments Issueing limit\n2\tequipments limit in stock\n3\tTime Limit")
                task_choice = int(input("Enter task choice from above catelog : "))
            
                if task_choice == 1:
                    doc_ref = db.collection('admin').document('equipments_issueing_limitation_database')
                    doc = doc_ref.get()
                    issue_limit = doc.to_dict()
                    
                    for i in range(0, len(issue_limit)):
                        issue_limit[game_choice][i] = input(f"issue limit for {game_database[game_choice][i]} : ")

                    doc_ref.update(issue_limit)

                elif task_choice == 2:
                    doc_ref = db.collection('admin').document('equipments_limitation_database')
                    doc = doc_ref.get()
                    limit = doc.to_dict()
                    
                    for i in range(0, len(limit)):
                        limit[game_choice][i] = input(f"limit for {game_database[game_choice][i]} in stock : ")

                    doc_ref.update(limit)

                elif task_choice == 3:
                    doc_ref = db.collection('admin').document('time_limitation_database')
                    doc = doc_ref.get()
                    time_limit = doc.to_dict()
                    
                    time_limit[game_choice] = input(f"time limit for issueing {game_choice} equipments : ")

                    doc_ref.update(time_limit)


            elif choice == 3:
                print(f"Thanks {self.admin}!!")

            else:
                print("wrong Choice. TRY again !!")

