import re
import django


sentence = input()
special_word = input()


pattern = rf'\b{special_word}\b'

result = re.findall(pattern, sentence, re.IGNORECASE)

print(len(result))
print(result)


#Примерен вход- The waterfall was so high, that the child couldn't see its peak.
#the