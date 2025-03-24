def validate_password(password):
    errors = []

    # Проверка за дължина
    if not (6 <= len(password) <= 10):
        errors.append("Password must be between 6 and 10 characters")

    # Проверка за съдържание (само букви и цифри)
    if not password.isalnum():
        errors.append("Password must consist only of letters and digits")

    # Проверка за поне 2 цифри
    digit_count = sum(char.isdigit() for char in password)
    if digit_count < 2:
        errors.append("Password must have at least 2 digits")

    # Извеждане на резултатите
    if errors:
        for error in errors:
            print(error)
    else:
        print("Password is valid")


# Тест
password = input("Enter a password: ")
validate_password(password)


#направена е с chatgpt  за да мога да я разбера защото не знаех как да я направя