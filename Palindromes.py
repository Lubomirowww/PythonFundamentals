def palindromes (nums):

    for num in nums:

        if num == num[:: -1]:
            print("True")

        else:
            print("False")





numbers= input().split(' ')
palindromes(numbers)