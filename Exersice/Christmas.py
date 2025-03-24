quantity = int(input())
days = int(input())

ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15

christmas_spirits = 0
sum_spent = 0
for day_number in range(1,days+1):
    if day_number % 11 == 0:
        quantity += 2
    if day_number % 2 == 0:
        sum_spent += ORNAMENT_SET * quantity
        christmas_spirits += 5
    if day_number % 3 == 0:
        sum_spent += (TREE_SKIRT * quantity + TREE_GARLANDS * quantity)
        christmas_spirits += 13

    if day_number % 5 == 0:
        sum_spent += TREE_LIGHTS * quantity
        christmas_spirits += 17
        if day_number % 3 == 0:
            christmas_spirits += 30


    if day_number % 10 == 0:
        christmas_spirits -= 20
        sum_spent += TREE_LIGHTS + TREE_GARLANDS + TREE_SKIRT

    if day_number == days and day_number % 10 == 0:
        christmas_spirits -= 30


print (f"Total cost: {sum_spent}")
print (f"Total spirits: {christmas_spirits}")

