import random

while True:
    choices=["rock","paper","scissor"]

    computer=random.choice(choices)

    player=None
    
    while player not in choices:
        player=input("rock, paper or scissor? ").lower()
        
    if player == computer:
        print("Computer: ", computer)
        print("Player: ",player)
        print("Tie!")
        
    elif player == "rock":
        if computer=="paper":
            print("Computer: ", computer)
            print("Player: ",player)
            print("You lose")
            
        if computer == "scissor":
            print("Computer: ", computer)
            print("Player: ",player)
            print("You win")
            
    elif player == "paper":
        if computer=="scissor":
            print("Computer: ", computer)
            print("Player: ",player)
            print("You lose")
            
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ",player)
            print("You win")
            
    elif player == "scissor":
        if computer=="rock":
            print("computer: ", computer)
            print("Player: ",player)
            print("You lose")
            
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ",player)
            print("You win")
    
    play_again=input("play again? : (yes/no)").lower()
    
    if play_again != 'yes':
        break
    
print("Bye!")