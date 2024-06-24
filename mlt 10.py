
# МЕТОДЫ СПИСКОВ # # ИЗMЕНЕНИЯ И ИЗМЕНЯЕМЫЕ КОРТЕЖИ #
# Homework 5 #

immutable_var = 7, 5, 3, True, "Корабль"
tuple_ = (immutable_var)
print(type(tuple_))
print(tuple_)
#tuple_[0] = 10      # кортеж не меняет данные : TypeError: 'tuple' object does not support item assignment

mutable_list = [6, 4, 9, 'a', 'Сокол']
list = (mutable_list)
print(type(list))
print(list)
list[1] = 'Арбуз'
list[4] = '101'
print(list)