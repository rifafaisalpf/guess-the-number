#MINI PROJECT
#GUESS THE NUMBER
import random

def guess_the_number():
    choice="yes"
    while choice=="yes":
        difficulty=input("difficulty level(easy,medium,hard):").lower()
        while difficulty not in ["easy","medium","hard"]:
            difficulty=input("difficulty level(easy,medium,hard):").lower()
        if difficulty=="easy":
            target =random.randint(1,50)
            max_attempts=10
            max_range=50
        elif difficulty=="medium":
            target=random.randint(1,100)
            max_attempts=5
            max_range=100
        elif difficulty=="hard":
            target=random.randint(1,200)
            max_attempts=3
            max_range=200
    
           
            
        num=0
        attempt=0
        while (num !=target and max_attempts > attempt):
            num=int(input("Guess the number:"))
            
            if  num >max_range or num<1 :
                print ("PLEASE ENTER A VALID NUMBER")
            else:
                attempt+=1
            
                if num == target :
                    print("YOU CORRECTLY GUESSED THE NUMBER")
                    print("YOU GUESSED THE NUMBER WITH",attempt,"ATTEMPTS")

                elif attempt==max_attempts:
                    print("YOU HAVE ALREADY USED ALL YOUR ATTEMPTS")
                    print("YOU LOSE THE GAME")
                    
                elif num>target :
                    print("YOUR NUMBER IS GREATER THAN THE TARGET NUMBER")
                        
                                    
                else:
                    print("YOUR NUMBER IS LESS THAN THE TARGET NUMBER")

        print("DO YOU WANT TO PLAY AGAIN?")
        choice=str(input("Enter your choice(YES or NO):")).lower()
               
guess_the_number()

