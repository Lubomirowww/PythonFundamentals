def print_func(legendary_items, junk_items, special_item):
    print(f"{special_item} obtained!")
    for item, quantity in sorted(legendary_items.items(), key=lambda x: (-x[1], x[0])):
        print(f"{item}: {quantity}")
    for item, quantity in sorted(junk_items.items()):
        print(f"{item}: {quantity}")

def legendary_farming():
    legendary_items_dict = {"shards": 0, "fragments": 0, "motes": 0}
    junk_items = {}

    while True:
        items = input().lower().split()
        for value, material in zip(items[0::2], items[1::2]):
            value = int(value)
            material = material.lower()

            if material in legendary_items_dict:
                legendary_items_dict[material] += value
                if legendary_items_dict[material] >= 250:
                    legendary_items_dict[material] -= 250
                    if material == "shards":
                        special_item = "Shadowmourne"
                    elif material == "fragments":
                        special_item = "Valanyr"
                    elif material == "motes":
                        special_item = "Dragonwrath"
                    print_func(legendary_items_dict, junk_items, special_item)
                    return  # спира цялата функция
            else:
                if material not in junk_items:
                    junk_items[material] = value
                else:
                    junk_items[material] += value

legendary_farming()
