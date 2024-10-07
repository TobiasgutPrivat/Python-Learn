Weight: float = float(input("Enter Weight? (in kilograms) "))
Height: float = float(input("Enter Height? (in meters) "))

BMI = Weight / (Height * Height)




if BMI < 18.5:
    print("Your BMI is", round(BMI,2), "which means the patient is underweight.")
elif 18.5 <= BMI < 25:
    print("Your BMI is", round(BMI,2), "which means the patient has a normal weight.")
elif 25 <= BMI < 30:
    print("Your BMI is", round(BMI,2), "which means the patient is overweight.")
elif BMI >= 30:
    print("Your BMI is", round(BMI,2), "which means the patient has obesity.")