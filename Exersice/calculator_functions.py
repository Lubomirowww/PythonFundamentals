def calculator(a, b, operator):

    if operator == "Multiple" or "multiple":
        return a * b

    elif operator == "Divide" or "divide":
        return a / b

    elif operator == "Add" or "add":
        return a ++ b

    elif operator == "Subtract" or "subtract":
        return a-b

print(calculator(operator=input("Въведете вид операция: "), a=int(input("Въведете число: ")), b=int(input("Въведете число: "))))


#lambda
#plus_five = lambda a: a+5