def capitals():
    countries_data = input().split(", ")
    capitals_data = input().split(", ")
    result = dict(zip(countries_data,capitals_data))
    print(result)


    for country, capital in result.items():
        print(f"{country} -> {capital}")


capitals()
# Тук всяка държава е с нейната столица
#  Като ги въвеждаме като ключ който е държавата, а стойноста е столицата
# С ZIP ги обединяваме