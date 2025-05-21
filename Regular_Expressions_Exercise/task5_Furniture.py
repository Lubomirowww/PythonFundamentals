import re




def furniture_info():

    pattern = r">>([A-Za-z]+)<<(\d+(?:\.\d+)?)!(\d+)"

    spend_money= 0
    product_list = []


    while True:
        data = input()

        if data == "Purchase":
            break

        result  = re.search(pattern, data)
        print(result)

        if result is not None:
            product = result[1]
            price = float(result[2])
            quantity = float(result[3])
            spend_money += price * quantity
            product_list.append(product)


    print("Bought Furniture: ")


    if spend_money > 0 :
        print('\n'.join(product_list))

    print(f"Total money spend: {spend_money:.2f}")










furniture_info()






