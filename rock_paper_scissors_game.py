import sys
import getpass

print ("Welcome to the game of Rock Paper Scissors")

def PlayerNames():
    global player1
    global player2
    player1 = input("Please enter your name:")
    player2 = input("Please enter your name:")
    menu()

def menu():
    choice = input("\nwhat do you want to do? \n"
                   " 1. Start a new game \n"
                   " 2. Change Player name \n"
                   " 3. Quit game \n"
                   "choose(1, 2, 3)")
    if choice == "1":
        NewGame()
    elif choice == "2":
        PlayerNames()
    elif choice == "3":
        sys.exit("3 chosen")
    else:
        print("invalid option")

def NewGame():
    print ("starting a new game of Rock Paper Scissors")
    print ("Instructions: Use r(ock), p(aper), s(cissors) as input")
    allowed = ['r', 'p', 's']
    #using getpass module here to hide the input.
    play1choice = getpass.getpass(prompt = "player1, enter your choice:")
    if play1choice not in allowed:
        print("invalid input")
        #continue
    
    play2choice = getpass.getpass(prompt = "player2, enter your choice:")
    if play2choice not in allowed:
        print("invalid input")
        #continue
    
    else: 
        if play1choice == play2choice:
            print ("its a tie")
            menu()
        elif play1choice == 'r' and play2choice == 's':
            print("the winner is " + player1)
        elif play1choice == 's' and play2choice == 'p':
            print("the winner is " + player1)
        elif play1choice == 'p' and play2choice == 'r':
            print("the winner is " + player1)
        else:
            print(player2 + " is the winner")
        menu()
        
PlayerNames()
