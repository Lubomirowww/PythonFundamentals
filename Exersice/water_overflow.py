number=int(input())
capacity = 0

for _ in range(number):

    liters = int(input())

    if liters + capacity <= 255:
        capacity += liters
        continue

    print("Insufficeient capacity!")

print(f"Liters is:{capacity}")
