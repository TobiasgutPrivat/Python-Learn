CapsuleWeight: float = 100
DosePerKg: float = 5 # assumed 0.5mg/kg

BodyWeight = float(input("What is your Body Weight? (in kg) "))

Dose = DosePerKg * BodyWeight # in mg
print(f"The total dosage of the medicine the patient should take is: {round(Dose,0)} mg")
print(f"The number of complete packages of medicine required is: {round(Dose / CapsuleWeight,0)}")
print(f"The deficit in the prescribed medicine is: {Dose % CapsuleWeight} mg")
