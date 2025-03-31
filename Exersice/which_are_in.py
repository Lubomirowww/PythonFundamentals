elements= input().split(', ')
sentence=input()
result =[el for el in elements if el in sentence]

print(result)