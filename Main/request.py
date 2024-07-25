import json

class Request:

    def game_choice(self):

        print('''
            \t1   Cricket
            \t2   Badminton
            \t3   volleyball
        ''')

        game = int(input("Enter your choice from above cateloge : "))

        if game == 1:
            self.cricket()
        
        elif game == 2:
            self.badminton()

        elif game == 3:
            self.volleyball()

    def cricket(self):
        
        print("Give quantity of each item : ")
        
        cricket_bat = int(input("\tCricket Bat : "))
        cricket_ball = int(input("\tCricket Ball : "))
        strumps = int(input("\tStrumps : "))
        bails = int(input("\tBails : "))

        