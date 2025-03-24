nums = input().split(' ')
copy_nums = list(map(int, nums)) #map прави от стринг интиджър
count = int(input())

for _ in range(count):

    current_min_element = min(copy_nums)
    nums.remove(str(current_min_element))
    copy_nums.remove(current_min_element)

print(', '.join(nums))
