
def calc_prize(product, quantity):

    if product == "Coffe":
        return quantity * 1.5

    elif product == "Coke":
        return quantity * 1.4

    elif product == "water":
        return quantity * 1

    elif product == "snacks":
        return  quantity * 2

current_product = input()
current_quantity = int(input())

final_prize=(calc_prize(current_product, current_quantity))

print(f"{final_prize:.2f}")