car_model = input("Изберете купе на автомобила:")
available_versions = {
    "Sedan"
    "SUV"
    "Coupe"
}
car_brand = input("Изберете марка на кола: ")
car_color = input("Изберете цвят на колата: ")
price = 0
features = []



available_features = {

    "navigation": 1500,
    "leather seats": 2000,
    "panorama": 1000,
}
print(available_features)
user_input = input("Въведи избраните екстри:")




equipment_features = [f.strip().lower() for f in user_input.split(", ")]

for feature in equipment_features:
    if feature in available_features:
        features.append(feature)
        price += available_features[feature]
    else:
        print(f"{feature} не е валидна екстра и ще бъде пропусната.")


if car_model == "Sedan":
    price += 20000

elif car_model == "SUV":
    price += 30000

elif car_model == "Coupe":
    price += 25000

print(f"\nКолата е {car_model} в цвят {car_color}.")
print(f"Избрани екстри: {', '.join(features)}")
print(f"Крайна цена: {price} лв")


