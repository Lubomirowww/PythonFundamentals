# number=float(input())
# if number == 0:
#     print("Zero")
# elif 0 < number < 1:
#     print("small positive")
# elif number >= 1:
#     print("positive")
# elif number > 1 and number > 1000000:
#     print("Large")
# else:
#     print("negative")

#for loop:
# for x in range (10):
#     if x == 9:
#
#         break
#
#     print(x)

word = input()


for i in range(len(word)-1, -1, -1  ):
    print(word[i])