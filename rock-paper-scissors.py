import random

options = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
ties = 0

print("Rock Paper Scissors!")

while True:
    player = input("\nEnter rock, paper, or scissors (or quit): ").lower()
    
    if player == "quit":
        print("\nFinal Score:")
        print("You:", player_score)
        print("Computer:", computer_score)
        print("Ties:", ties)
        print("Thanks for playing!")
        break
    
    if player not in options:
        print("Invalid choice, try again.")
        continue
    
    computer = random.choice(options)
    print("Computer chose:", computer)
    
    if player == computer:
        print("It's a tie!")
        ties += 1
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    print("Score — You:", player_score, "| Computer:", computer_score, "| Ties:", ties)
