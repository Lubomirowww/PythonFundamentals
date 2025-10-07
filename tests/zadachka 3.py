n = int(input("Въведи число N: "))
number = 1
total = 0

while number <= n:
    if number % 2 == 0:
        total += number
    number += 1

print("Сборът на четните числа е:", total)

