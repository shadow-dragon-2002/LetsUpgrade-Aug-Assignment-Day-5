

def Guessing_game():
    import random
   
    score = 0                                                                                                #variables for while loop and startinf score
    again = "y"
    
    while again == "y" :                                                                                     #while loop that goes tll user/player enter n
        correct_guess = random.randint(1,50)                                                                 #assigns a random number between 1-50 and asks user to guess after that takes difference between them.
        guess = int(input("Enter your guess: "))

        difference = correct_guess - guess
        
        if correct_guess == guess :                                                                          #conditionals for each scenario of guessed number
            print("Damn you guessed it right, you must have some superpowers. ;) You scored 10/10")
            score = score + 10
            
        elif difference >= -5 and difference <= 5 :
            print("Almost correct but slightly off. Your scored 5 points")
            score = score + 5
            
        else:
            print("Sorry wrong guess. You scored 0")
        
        print ("The correct guess was: " + str(correct_guess))
        print ("Your total score: " + str(score))
        
        again = str(input("Do you want to play again ? (y/n) : "))                                            #asking user/player if they want to play again.
    
    if score == 0:                                                                                            #final scores and remarks.
        print("Better luck next time. Your final score is" + str(score)) 
    else:
        print("Not bad you scored " + str(score))   
    print("Thank you for playing Balamurali's guessing game. Hope you had fun. :)")
        

Guessing_game()
        