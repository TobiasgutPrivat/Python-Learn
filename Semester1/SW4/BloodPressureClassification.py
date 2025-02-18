systolic = int(input("Enter the patient's systolic blood pressure: "))
diastolic = int(input("Enter the patient's diastolic blood pressure: "))

if systolic < 120 and diastolic < 80:
    print("The patient has normal blood pressure.")
elif 120 <= systolic <= 129 and diastolic < 80:
    print("The patient has elevated blood pressure.")
elif 130 <= systolic <= 139 or 80 <= diastolic <= 89:
    print("The patient is in Hypertension Stage 1.")
elif systolic >= 140 or diastolic >= 90:
    if systolic >= 180 or diastolic >= 120:
        print("The patient is in a hypertensive crisis. Seek immediate medical attention.")
    else:
        print("The patient is in Hypertension Stage 2.")
else:
    print("Invalid readings. Please check the blood pressure values.")