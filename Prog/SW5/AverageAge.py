def inputInt(text: str) -> int:
    while True:
        value = input(text)
        if value.isdigit():
            return value
        else:
            print("Invalid input")

people = int(inputInt("How many people? "))
ages = []
for i in range(people):
    ages.append(int(inputInt(f"Age of person {i+1}? ")))
print(f"Average age: {sum(ages) / len(ages)}")