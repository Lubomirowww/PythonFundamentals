number=int(input())

negatives=list()
positives=list()
sum_of_negatives=0

for i in range(number):

    current_num=int(input())
    if current_num >=0:
        positives.append(current_num)

    else:
        negatives.append(current_num)
        sum_of_negatives += current_num

print(positives)
print(negatives)
print(f"Count of positives:{len(positives)}")
print(f"Sum of negatives:{sum_of_negatives}")
