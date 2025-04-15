data = input()
store = dict()

while data != "statistics":

    data = data.split(": ")

    product = data[0]
    quantity = int(data[1])

    if product in store.keys():
        store[product] += quantity

    else:
        store[product] = quantity

    data = input()


count = len(store.keys())
total = sum(store.values())

print(f"Products in stock: ")

for product in store:
    print(f". {product}: {store[product]}")

print(f"Total products: {count}")
print(f"Total quantity: {total}")

