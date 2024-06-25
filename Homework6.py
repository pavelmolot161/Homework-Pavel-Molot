
   # СЛОВАРИ И МНОЖЕСТВА #

# phone_book = {'Павел': 88005556767, 'Олег': 88004563456}
# print(phone_book)
# phone_book = {['Павел']: 88005556767, 'Олег': 88004563456} # TypeError: unhashable type: 'list'
# print(phone_book)

# phone_book = {'Павел': 88005556767, 'Олег': 88004563456}
# print(phone_book ['Павел'])
# phone_book['Павел'] = 89999998888
# phone_book['Антон'] = 89004445566
# del (phone_book)['Олег']
# phone_book.update({'Саша': 87006005544,
#                    'Максим': 89004443333})
# print(phone_book)

# phone_book = {'Павел': 88005556767, 'Олег': 88004563456}
# print(phone_book ['Павел'])
# phone_book['Павел'] = 89999998888
# phone_book['Антон'] = 89004445566
# del (phone_book)['Олег']
# phone_book.update({'Саша': 87006005544,
#                    'Максим': 89004443333})
# print(phone_book)
# print(phone_book.get('Антон'))
# print(phone_book.get('Марина', 'Такого ключа нет'))
# print(phone_book)
# phone_book.pop('Антон')
# a = phone_book.pop('Антон')
# print(phone_book)
# print(a)

# phone_book = {'Павел': 88005556767, 'Олег': 88004563456}
# phone_book.update({'Саша': 87006005544,
#                    'Максим': 89004443333})
# a = phone_book.pop('Саша')
# list_ = [1, 2, 3]
# list_.pop(0)
# print(list_)
# print(phone_book)
# print(a)

# phone_book = {'Павел': 88005556767, 'Олег': 88004563456,
#               'Дима': 89007776665}
# phone_book.update({'Саша': 87006005544,
#                    'Максим': 89004443333})
# print(phone_book.keys())

# phone_book = {'Павел': 88005556767, 'Олег': 88004563456,
#               'Дима': 89007776665}
# phone_book.update({'Саша': 87006005544,
#                    'Максим': 89004443333})
# print(phone_book.values())

# phone_book = {'Павел': 88005556767, 'Олег': 88004563456,
#               'Дима': 89007776665}
# phone_book.update({'Саша': 87006005544,
#                    'Максим': 89004443333})
# print(phone_book.items())

   # МНОЖЕСТВА #

# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4}
# print(set_)

#set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
#print(set_)

# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
# list_ = [1, 1, 1, 1, 2, 3, 2, 2]
# print(set(list_)  # множество
# print(list_[0])

# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
# list_ = [1, 1, 1, 1, 2, 3, 2, 2]
# list_ = set(list_)
# print(list_[0]) # ОШИБКА TypeError: 'set' object is not subscriptable

# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
# list_ = [1, 1, 1, 1, 2, 3, 2, 2]
# list_ = set(list_)
# print(list_.discard(1))
# print(list_)

# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
# list_ = [1, 1, 1, 1, 2, 3, 2, 2]
# list_ = set(list_)
# print(list_.remove(1))
# print(list_)

# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
# list_ = [1, 1, 1, 1, 2, 3, 2, 2]
# list_ = set(list_)
# print(list_.add(5))
# print(list_)

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








