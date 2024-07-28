import json

class Request:

    email = None

    def __init__(self, e_mail):
        self.email = e_mail

    def game_file_reader(self):
        

    def game_choice(self):

        print('''
            \t1     Cricket
            \t2     Badminton
            \t3     volleyball
            \t4     chess
            \t5     Tenis
            \t6     Basketball
            \t7     Football
        ''')

        game = int(input("Enter your choice from above cateloge : "))

        if game == 1:
            self.cricket()
        
        elif game == 2:
            self.badminton()

        elif game == 3:
            self.volleyball()

        elif game == 4:
            self.Tennis()
        
        elif game == 5:
            self.Basketball()

        elif game == 6:
            self.Football()

    def cricket(self):
        
        print("Give quantity of each item : ")
        
        cricket_bat = int(input("\tCricket Bat : "))
        cricket_ball = int(input("\tCricket Ball : "))
        strumps = int(input("\tStrumps : "))
        bails = int(input("\tBails : "))

        data = [0, [
            cricket_bat,
            cricket_ball,
            strumps,
            bails
        ]]

        return data
    
    def badminton(self):
        
        print("Give quantity of each item : ")
        
        badminton_racket = int(input("\tBadminton Racket : "))
        shuttlecock = int(input("\tShuttlecock : "))

        data = [1, [
            badminton_racket,
            shuttlecock
        ]]

        return data
    
    def volleyball(self):

        print("Give quantity of each item : ")
        volleyball = int(input("\tVolleyball : "))

        data = [2, [
            volleyball
        ]]

        return data
    
    def Tennis(self):

        print("Give quantity of each item : ")
        tennis_racket = int(input("\tTennis Racket : "))
        tennis_ball = int(input("\tTennis Ball : "))
        data = [3, [
            tennis_racket,
            tennis_ball
        ]]

        return data

    def Basketball(self):

        print("Give quantity of each item : ")
        basketball = int(input("\tBasketball : "))

        data = [4, [
            basketball
        ]]

        return data

    def Football(self):

        print("Give quantity of each item : ")
        football = int(input("\tFootball : "))

        data = [5, [
            football
        ]]

        return data






data = {
            "Cricket" : {
                "Cricket Bat" : cricket_bat,
                "Cricket Ball" : cricket_ball,
                "Strumps" : strumps,
                "Bails" : bails
            }
        }
[0,[1,1,1,1]]
data = {
            "Badminton" : {
                "Badminton Racket" : badminton_racket,
                "shuttlecock" : shuttlecock
            }
        }
[1,[1,1]]
data = {
            "Volleyball" : {
                "Volleyball" : volleyball
            }
        }
[2,[1]]
data = {
            "Tennis" : {
                "Tennis Racket" : tennis_racket,
                "Tennis Balls" : tennis_ball
            }
        }
[3,[1,1]]
data = {
            "Basketball" : {
                "Basketball" : basketball
            }
        }
[4,[1]]
data = {
            "Football" : {
                "Football" : football
            }
        }
[5,[1]]