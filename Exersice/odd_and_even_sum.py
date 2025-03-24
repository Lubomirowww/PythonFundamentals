def odd_even_sum(nums):
    odd_sum=0
    even_sum=0
    for num in nums:
        if num % 2 == 0:
            even_sum += num

        else:
            odd_sum += num

    print(odd_sum, even_sum)




numbers = map(int, list(input()))
odd_even_sum(numbers)
