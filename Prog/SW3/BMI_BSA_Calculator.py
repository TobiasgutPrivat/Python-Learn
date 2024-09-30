Weight: float = float(input("What is your Weight? (in kilograms) "))
Height: float = float(input("What is your Height? (in meters) "))

BMI = Weight / (Height * Height)
print("Your Body Mass Index (BMI) is: ", round(BMI,2))
