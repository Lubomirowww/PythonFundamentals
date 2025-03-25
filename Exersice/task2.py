num_wagons = int(input("Номер на вагон:"))

train= [0 for i in range(num_wagons)]

command = input()

while command != "End":

    explode = command.split(" ")
    current=explode[0]
    if current == "Add":
        num_people = int(explode[1])
        train[ - 1] += num_people



    if current == "Insert":
        position= int(explode[1])
        num_people = int(explode[2])
        train[position] += num_people




    if current == "Leave":

        position = int(explode[1])
        num_people = int(explode[2])
        train[position] -= num_people

    command = input()

print(train)


