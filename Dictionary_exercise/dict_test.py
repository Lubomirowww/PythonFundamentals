person = {'name': 'Mike', 'gender': 'M', 'age': 19}
#          key     value   key      value  key  value

test = person.keys()#Ивикаваме ключовете
test1 = person.values()#Ивикаваме стойностите на ключовете
test2 = person.items()#Така извикваме всичко което има в речника
person.pop('name')#Махнахме ключа "name" и неговата стойност
test3 = person.get("age")#Извикваме стойноста от съответния ключ
test4 = person.clear()#Изчистваме речника
print(person)
print(test3)
print(test4)

test5= ("arg1", 'arg2', 'arg3', 'arg4')
val = [1, 2, 3, 4]
my_dict = dict.fromkeys(test5, val)
my_dict2 = dict(zip(test5, val))
print(my_dict)
print(my_dict2)