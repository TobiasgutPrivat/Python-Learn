class appointment:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __str__(self):
        return f"Patient: {self.name}, {self.time}"
    
def inputValidated(text: str, validate: callable) -> str:
    while True:
        value = input(text)
        if validate(value):
            return value
        else:
            print("Invalid input")
    
appointments: list[appointment] = []

while True:
    print()
    print("Menu")
    print("1. Schedule an appointment")
    print("2. Remove an appointment")
    print("3. View appointments")
    print("4. Exit")
    choice = int(inputValidated("Enter your choice (1/2/3/4): ", lambda x: x.isdigit() and 1 <= int(x) <= 4))
    print()
    if choice == 1:
        name = input("Enter patient's name: ")
        time = input("Enter appointment time: ")
        appointments.append(appointment(name, time))
        print(f"Appointment scheduled for {name} at {time}")
    elif choice == 2:
        name = input("Enter patient's name: ")
        for appointment in appointments:
            if appointment.name == name:
                appointments.remove(appointment)
                print(f"Appointment removed for {name}")
                break
        else:
            print("Appointment not found")
    elif choice == 3:
        print("Scheduled Appointments:")
        for i in range(len(appointments)):
            print(f"{i+1}. {appointments[i]}")
    elif choice == 4:
        break
    else:
        print("Invalid choice")