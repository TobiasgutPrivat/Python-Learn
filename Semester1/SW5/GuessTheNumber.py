import random

def inputValidated(text: str, validate: callable) -> str:
    while True:
        value = input(text)
        if validate(value):
            return value
        else:
            print("Invalid input")

number: int = random.randint(1, 10)
guess: int = 0

print("A random number got generated")
print("Guess the number between 1 and 10")

while guess != number:
    guess = int(inputValidated("Enter your guess: ", lambda x: x.isdigit() and 1 <= int(x) <= 10))
    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else:
        print("You guessed it correctly")
