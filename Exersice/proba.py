def grade_text():

 grade = float(input("Въведи оценка: "))

 if 2.00 <= grade <= 2.99:
    print(f"{grade} Fail")

 if 3.00 <= grade <= 3.49:
    print(f"{grade} Poor")

 if 3.50 <= grade <= 4.49:
    print(f"{grade} Good")

 if 4.50 <= grade <= 5.49:
    print(f"{grade} Very Good")

 if 5.50 <= grade <= 6.00:
    print(f"{grade} Excellent")

 else:
    print("Error")

print(grade_text())
print(grade_text())
print(grade_text())