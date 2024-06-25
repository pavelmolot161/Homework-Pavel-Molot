

#  Homework 6 #  # СЛОВАРИ #

my_dict = {'Павел': 2000, 'Олег': 1999}
print(my_dict)
print(my_dict ['Павел'])
print(my_dict.get('Полина', 'без ошибки'))
print(my_dict)
my_dict.update({'Саша': 1996,
                'Максим': 2005})
a = my_dict.pop('Олег')
print(a)
print(my_dict)

   # МНОЖЕСТВА #

my_set = {7, 9, 12, 7, 9, 8, 12, 9, 6, 6, 8,'Облако', True, (1, 2, 3)}
print(my_set)
my_set = set(my_set)
print(my_set.add(55))
print(my_set.add("Дом"))
print(my_set)
print(my_set.discard(1))
print(my_set)








