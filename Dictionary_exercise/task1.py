from collections import Counter

word = input()
result = Counter (word)


print(result)#Става и така обаче така няма как да изолираме празните пространства ако има такива
# for key, value in result.items():
#     if key != " ":
#         print(f"{key} ->{value}")