def miner_task():
    my_dict = {}
# Shift + F6 сменяме името на променливата в целия код

    while True:
        resource = input()

        if resource == "Stop":
            break


        quantity = int(input())

        if resource not in my_dict:
            my_dict[resource] = quantity
        else:
            my_dict[resource] += quantity

    for key, value in my_dict.items():
        print(f"{key} -> {value}")

miner_task()
# В тази задача въвеждаме вид продукт и неговото количество
# При команда Стоп програмата приклюва и показва от кой
# Продукт колко количество има