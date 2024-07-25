import json

class Login:

    def __init__(self):
        
        # aking for registering or login
        reply = input ("\tWelcome !! are you registered (Y/N) : " )

        # for login
        if reply == "y" or "Y":
            self.login()

        # for registering
        if reply == "N" or "n":
            self.register()

    def login(self):

        login_username = input("Enter your username : ")
        login_password = input("Enter your password : ")

    
    def register(self):
        
        username = input ("Username : ")        
        self.check(username, 1)
        password = input("Password : ")
        self.update_list(username, password)

    # checking the login data of file to check if username is taken or not.
    def check(self, id_dict):
        
        with open ("logins_list.json", 'r') as file:
            data = json.load(file)
        
        if len(id_dict) == 1:
            if id_dict[0] in list(data.keys()):
                print("This username is not available")
                self.register()

        elif len(id_dict) == 2:
            if id_dict in data:
                print (f"\t\t<------- Welcome {id_dict[0]} ------->")

    # for storing usernae and password in database
    def update_list(self, username, password):

        with open ("logins_list.json", 'r') as file:
            data = json.load(file)
        
        new_data = {username : password}

        # updating the data in variable
        data.update(new_data)

        #updating data in file
        with open ("logins_list.json", 'w') as file:
            json.dump(data, file, indent = 4)
        
        print (f"\t\tRegistered as {username} successfully !!")
