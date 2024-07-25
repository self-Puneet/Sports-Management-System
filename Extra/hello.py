import json

class login 







class Request:
    
    Name = "Puneet"
    Enrollment_Number = "23CS002726"
    Programme = "B.Tech"
    Year = 2023
    
    def __init__(self, name, enrollment_number, programme, year):
        Name, Enrollment_Number, Programme, Year = name, enrollment_number, programme, year
    
    def request(self, game):
        
        if game == "Cricket" or "cricket":
            Cricket_Bat = input("\tCricket Bat   : ")
            Cricket_Ball = input("\tCricket Ball  : ")
            Stumps = input("\tStumps        : ")
            Bails = input("\tBails         : ")
            Time_Request = input("\t\tTime Reques  : ")

            data = {
                "Name" : self.Name,
                "Enrollment Number" : self.Enrollment_Number,
                "Programme" : self.Programme,
                "Year" : self.Year,
                "Time Requested" : Time_Request,
                "item requested" : {
                    "Cricket Bat" : Cricket_Bat,
                    "Cricket Ball" : Cricket_Ball,
                    "Stumps" : Stumps,
                    "Bails" : Bails
                },
                "status" : "pending"
            }

            with open ("requests.json", "w") as file:
                json.dump (data, file, indnet = 4)

        elif game == "Badminton" or "badminton":
            Badminton_Racket = input("\tBadminton Racket  : ")
            Shuttlecock =      input("\tShuttlecock       : ")

            data = {
                "Name" : self.Name,
                "Enrollment Number" : self.Enrollment_Number,
                "Programme" : self.Programme,
                "Year" : self.Year,
                "Time Requested" : Time_Request,
                "item requested" : {
                    "Badminton Racket" : Badminton_Racket,
                    "Shuttlecock" : Shuttlecock
                },
                "status" : "pending"
            }

            with open ("requests.json", "w") as file:
                json.dump (data, file, indent = 4)

    