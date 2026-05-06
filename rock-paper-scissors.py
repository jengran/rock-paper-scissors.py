Python 3.13.1 (main, Jan 16 2025, 13:50:41) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
... 
... options = ["rock", "paper", "scissors"]
... 
... print("Rock Paper Scissors!")
... 
... while True:
...     player = input("\nEnter rock, paper, or scissors (or quit): ")\
.lower()
...     
...     if player == "quit":
...         print("Thanks for playing!")
...         break
...     
...     if player not in options:
...         print("Invalid choice, try again.")
...         continue
...     
...     computer = random.choice(options)
...     print("Computer chose:", computer)
...     
...     if player == computer:
...         print("It's a tie!")
...     elif (player == "rock" and computer == "scissors") or \
...          (player == "paper" and computer == "rock") or \
...          (player == "scissors" and computer == "paper"):
...         print("You win!")
...     else:
...         print("Computer wins!")
...         
Rock Paper Scissors!





Enter rock, paper, or scissors (or quit): rock
Computer chose: rock
It's a tie!






Enter rock, paper, or scissors (or quit): paper
Computer chose: paper
It's a tie!






Enter rock, paper, or scissors (or quit): paper
Computer chose: scissors
Computer wins!

Enter rock, paper, or scissors (or quit): Enter rock, paper, or scisso\
rs (or quit): paperComputer chose: paperIt's a tie!Enter rock, paper, \
or scissors (or quit): 
