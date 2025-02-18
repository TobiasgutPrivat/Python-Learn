def CaesarEncryption(distance: int, text: str) -> str:
    lower_text = text.lower()    

    result: str = ""
    for c in lower_text:
        ordinal = ord(c)

        if ordinal >= 97 and ordinal <= 122:
            ordinal += distance % 26
            if ordinal > 122:
                ordinal -= 26
            if ordinal < 97:
                ordinal += 26
        else:
            continue

        result += chr(ordinal)
    return result


def encrypt(text: str) -> str:
    return CaesarEncryption(-3, text)

def decrypt(text: str) -> str:
    return CaesarEncryption(3, text)

while True:
    print("1. Encrypt\n2. Decrypt\n3. Exit")
    inputstr = input()
    if not inputstr.isdigit():
        print("Invalid input")
        continue

    choice = int(inputstr)

    if choice == 1:
        text = input("Enter text: ")
        text = encrypt(text)
        print(text)
    elif choice == 2:
        text = input("Enter text: ")
        text = decrypt(text)
        print(text)
    elif choice == 3:
        break
    else:
        print("Invalid input")