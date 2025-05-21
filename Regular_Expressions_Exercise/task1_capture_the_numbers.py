import re

pattern = r"\d+"


while True:

    text = input()

    if not text:
        break

    result = re.findall(pattern, text)

    if len(result) > 0:
        print(' '.join(result), end=' ')



#Примерен вход
#The300
#what is that?
#I think it's the 3rd movie
#Lets watch it at 22:45

