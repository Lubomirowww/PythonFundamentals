import re


data = input()


pattern = r'\b_[a-zA-Z0-9]+\b'


result = re.findall(pattern, data)

words_list = []

for word in result:
    words_list.append(word[1:])


print(' '.join(words_list))

#примерен вход - The _id and _age variables are both integers.

