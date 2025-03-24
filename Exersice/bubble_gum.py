str1 =  input()

str2 =  input()

result = ""
previous_str= str1

for index in range (len(str1)):
    for i in range (index+1):
        result += str2[i]

    for i in range (index+1, len(str1)):
        result += str1[i]
    if  not result == previous_str:
        print(result)

    previous_str = result
    result=""


