import datetime
current_year = datetime.datetime.now().year

age = input("What is your age? ")
birthYear = int(current_year) - int(age)
Year100 = int(birthYear) + 100
print("You were born in the year", birthYear)
print("You will be 100 years old in the year", Year100)
