number = int(input())
total_sum=0

for _ in range(number):
    char=input()
    total_sum += ord(char)

print(f"The sum equals:{total_sum}")

#Задачата сумира числата които отговарят на символите от
#Ascii таблицата.