import random
player1 = input("Enter a name for Player1: ")

user_lives = 0
lives = 0
choice=None 
game = ['Rock','Paper','Scissor']

def changeChoice(choice):
    newChoice = 0 
    newChoice = random.randint(1,3)
    if (newChoice==choice) :
        newChoice = changeChoice(choice)
    return (newChoice)

while (1):
    width = 30

    if lives==3 :
        print ("Computer Wins!!")
        break
    elif user_lives==3:
        print (player1," Wins!!")
        break
    else:
        choice = 0
        user_choice = input("\nEnter:\n1 for Rock,\n2 for Paper,\n3 for Scissors\n")
        choice = random.randint(1,3)

        if user_choice not in ['1','2','3']:
            print ("Invalid choice")
            continue 

        user_choice = int(user_choice)
        if choice==user_choice:
            choice = changeChoice(choice)

        print ("\nComputer's choice:%s and %s's choice:%s \n" % (game[choice-1].upper(), player1, game[user_choice-1].upper()))
        if choice == (user_choice + 1):
            lives+=1
        elif user_choice == (choice + 1):
            user_lives+=1
        elif user_choice < choice:
            user_lives+=1
        elif choice < user_choice:
            lives+=1
        elif user_choice == choice:
            pass
        else:
            print ("Something wrong")
        print ("{}| {}".format("Computer".ljust(width),player1.ljust(width)))
        print ("{}| {}".format(str(lives).ljust(width),str(user_lives).ljust(width)))

