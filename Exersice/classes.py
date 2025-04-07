class MyClassIsPerson:

    species = 'mammal'
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def say_hello(self, school):    #Метод-винаги се задава със self
        return f'Hello {self.first_name} {self.last_name} from {school}'






ivan = MyClassIsPerson('Ivan', 'Ivanov', 25) #Това е обект
print(ivan.first_name, ivan.last_name, ivan.age)

print(ivan.species)

