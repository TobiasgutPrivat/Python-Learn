password = 'asd1$aasd'
def check_password(password):
    if len(password) < 8:
        return False

    has_digit = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_digit = True
        if char in '$_.,/':
            has_special = True

    return has_digit and has_special

print(check_password(password))
