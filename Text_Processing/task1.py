text = input()

while text != "end":

    rev = (reversed(text))
    for char in rev:
        print(char, end="")

    text= input()