# number = 2
#
# if number == 5:
#     print(number)
# number += 1
# if number == 5:
#     print(number)
# number += 1
# if number == 5:
#     print(number)
# number += 1
# if number == 5:
#     print(number)
# number += 1

#task 4
# number = 2
# while number < 10:
#     print(number)
#     number += 2
#
# number = float(input())
#
# while number < 1 or number > 100:
#     number = float(input())
#
# print(f"The number {number} is between 1 and 100")

#task 5
number = int(input())

for i in range (number):
    for j in range (0, i+1):
        print ("*", end="")
    print()

for i in range (number-1):
    for j in range (number-1,i,-1):
      print("*", end="")
    print()