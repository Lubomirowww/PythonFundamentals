banned_words= input().split(", ")
text=input()

for word in banned_words:
    while word in text:
        text = text.replace(word, "*" * len(word))


print(text)

#Тази задача прави определен текст в звездички

#примерен вход
#Linux, Windows - това са думите които искаме да махнем
#It is not Linux, it is GNU/Linux.
# Linux is merely the kernel, while GNU adds the functionality.
# Therefore we owe it to them by calling the OS GNU/Linux! Sincerely,
# a Windows client

