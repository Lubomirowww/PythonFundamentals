text = input()

result_text = ""

for char in text:
    result_text += char * 2 #magic method когато умножаваме стринг по интеджър

print(result_text)