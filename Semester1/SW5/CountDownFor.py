import time

def inputInt(text: str) -> int:
    while True:
        value = input(text)
        if value.isdigit():
            return value
        else:
            print("Invalid input")

number: int = int(inputInt("Enter a number to count down from: "))

for i in range(number, 0, -1):
    time.sleep(1)
    print(i)