number=int(input())


numbers_list =list()

for i in range(number):

    current = int(input())
    numbers_list.append(current)


filtered_word = input()

filtered = list()

for current_num in numbers_list:

    if filtered_word == "Even":
        if current_num %2 == 0:
            filtered.append(current_num)

    if filtered_word == "Odd":
        if current_num %2 != 0:
            filtered.append(current_num)

    if filtered_word == "positive":
        if current_num >=0:
            filtered.append(current_num)

    if filtered_word == "negative":
        if current_num < 0:
            filtered.append(current_num)

print(filtered)



 