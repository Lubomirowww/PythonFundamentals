text=input()
digits = ""
letters = ""
chars = ""

for ch in text:
    if ch.isdigit():
        digits += ch

    elif ch.isupper() or ch.islower():
        letters += ch

    else:
        chars += ch


#Тази задача изкарва от входа символи числа и букви

print(digits)
print(letters)
print(chars)