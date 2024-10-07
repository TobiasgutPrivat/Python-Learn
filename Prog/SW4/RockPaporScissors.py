import random

print("Rock, Paper, Scissors")

while True:
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")

    playerMove = input()
    if playerMove == "q":
        break

    computerMove = random.choice(["r", "p", "s"])

    print(f"Computer plays {computerMove}")

    if playerMove == computerMove:
        print("It's a tie!")
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
    else:
        print("You lose!")

print("Thanks for playing!")