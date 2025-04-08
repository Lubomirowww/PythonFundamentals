#self- играе ролята на такси като обира данните и ги качва тук горе
class MyPerson:

    value = 50 # class attribute
    __number = 50 # Така защитаваме attribute

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.value = 30


    def say_hello(self): #това се нарича метод
        return f"Hello {self.first_name}"


obj = MyPerson('Mitko', 'Lubomirov')
obj2 = MyPerson(last_name='Mitko', first_name='Lubomirov')

print(obj.say_hello())#Така извикваме метода
print(MyPerson.value)
