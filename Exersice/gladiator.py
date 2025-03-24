lost_fights_count=int(input("Изгубени битки:"))
helmet_price = float(input("Цена за каска:"))
sword_price = float(input("Цена за меч:"))
shield_price = float(input("Цена за щит:"))
armor_price = float(input("Цена за броня:"))

gladiator_expenses = 0
shield_counter = 0

for lost in range(1,lost_fights_count+1):

    if lost % 2 == 0:
        gladiator_expenses += helmet_price

    if lost % 3 == 0:

        gladiator_expenses += sword_price

        if lost % 2 == 0:

            gladiator_expenses += shield_price
            shield_counter +=1

            if shield_counter == 2:

                gladiator_expenses += armor_price
                shield_counter = 0


print(f"Gladiator expenses: {gladiator_expenses:.2f} aureus")

