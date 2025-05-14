def caesar_cipher(text):
    result = [chr(ord(ch) +3) for ch in text]
    print(''.join(result))


text = input()
caesar_cipher((text))

# В тази задача въвеждаме текст от който текст
# взимаме всеки елемент и неговата стойсност от ASCII Table
# след което увеличваме стойноста на елемента с 3 и отпечатваме
# съответно символа който се намира на адрес след като сме го увеличили с 3!


# примерен вход
# Programing is cool!

# изхода от примерния вход
# Surjudplqj#lv#frro$