words = input().split(" ")
palindrome_words = list()
palindrome= input()


for word in words:
    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        palindrome_words.append(word)





print(palindrome_words)
palindrome_count = words.count(palindrome)
print(palindrome_count)