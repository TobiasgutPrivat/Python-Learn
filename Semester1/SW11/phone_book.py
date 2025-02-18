def print_numbers(numbers):
    """Print all contacts in the phone book."""
    if not numbers:
        print("Phone book is empty")
    else:
        print("\nPhone Book:")
        for name, number in numbers.items():
            print(f"{name}: {number}")
    print()

def add_number(numbers, name, number):
    """Add a new contact to the phone book."""
    numbers[name] = number
    print(f"Added {name} with number {number}")

def lookup_number(numbers, name):
    """Look up a phone number by name."""
    return numbers.get(name, None)

def remove_number(numbers, name):
    """Remove a contact from the phone book."""
    if name in numbers:
        del numbers[name]
        print(f"Removed {name} from phone book")
    else:
        print(f"Contact {name} not found in phone book")

def load_numbers(numbers, filename):
    """Load contacts from a file."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, number = line.strip().split(',')
                numbers[name] = number
        print(f"Successfully loaded contacts from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error loading file: {e}")

def save_numbers(numbers, filename):
    """Save contacts to a file."""
    try:
        with open(filename, 'w') as file:
            for name, number in numbers.items():
                file.write(f"{name},{number}\n")
        print(f"Successfully saved contacts to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print()

def main():
    numbers = {}  # Dictionary to store phone numbers
    filename = "phone_book.txt"  # Default filename for saving/loading

    while True:
        print_menu()
        try:
            choice = input("Enter choice (1-7): ")
            
            if choice == '1':
                print_numbers(numbers)
            
            elif choice == '2':
                name = input("Enter name: ")
                number = input("Enter number: ")
                add_number(numbers, name, number)
            
            elif choice == '3':
                name = input("Enter name to remove: ")
                remove_number(numbers, name)
            
            elif choice == '4':
                name = input("Enter name to lookup: ")
                number = lookup_number(numbers, name)
                if number:
                    print(f"Number for {name}: {number}")
                else:
                    print(f"No number found for {name}")
            
            elif choice == '5':
                filename = input("Enter filename to load (or press Enter for default 'phone_book.txt'): ")
                if not filename:
                    filename = "phone_book.txt"
                load_numbers(numbers, filename)
            
            elif choice == '6':
                filename = input("Enter filename to save (or press Enter for default 'phone_book.txt'): ")
                if not filename:
                    filename = "phone_book.txt"
                save_numbers(numbers, filename)
            
            elif choice == '7':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")

if __name__ == "__main__":
    main()
