divisor = int(input())
bound = int(input())

n = 0

for num in range(1,bound+1):
    if num % divisor == 0:
        n = num


print(n)

# divisor = int(input())
# bound = int(input())
#
# n = 0
#
# for num in range(bound, 0, -1):
#     if num % divisor == 0:
#         n = num
#         break
#
#
# print(n) Решение при което брой от
#       най-голямото към най-малкото