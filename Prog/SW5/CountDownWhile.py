import time

def inputInt(text: str) -> int:
    while True:
        value = input(text)
        if value.isdigit():
            return value
        else:
            print("Invalid input")

number: int = int(inputInt("Enter a number to count down from: "))

while number >= 0:
    print(number)
    time.sleep(1)
    number -= 1