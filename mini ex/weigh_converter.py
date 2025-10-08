weight = int(input("Enter your weight: "))
unit = input("Enter your unit Kilograms or Pounds (K/L): ")

if unit == "L":
    weight = weight * 2.205
    print(f"Your weigh is {round(weight, 1)} {unit}")
elif unit == "K":
    weight = weight / 2.205
    print(f"Your weigh is {round(weight, 1)} {unit}")
else:
    print(f"The {unit} is not valid! ")

