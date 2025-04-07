class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = list()
        self.fish = list()
        self.birds = list()

    def add_animal(self, species, name):
        if species == "mammals":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "birds":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammals":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result += f"Fish in {self.name}: {', '.join(self.fish)}"
        elif species == "birds":
            result += f"Birds in {self.name}: {', '.join(self.birds)}"

        result += f"\nTotal animals: {Zoo.__animals}"
        return result


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_lines = int(input())

for _ in range(number_of_lines):
    info = input().split(" ")
    species = info[0]
    type_of_animal = info[1]
    zoo.add_animal(species, type_of_animal)

additional_info = input()
print(zoo.get_info(additional_info))
