
# МЕТОДЫ СПИСКОВ #

#food = ["яблоко", "кокос", "банан"]
#print(food[0])
#food[0] = "кукуруза"
#print(food)

#food = ["яблоко", "кокос", "банан"]
#print(food[1])
#food[1] = "кукуруза"
#print(food)

#food = ["яблоко", "кокос", "банан"]
#food.append(True)
#print(food)
#food.extend(["абрикрс", 2])
#print(food)
#food.remove("яблоко")
#print(food)
#print("кокос" in food) # проверка в списке
#print("кокос" not in food)
#print(food[0:2:2])
#print(food[3])

# ИЗMЕНЕНИЯ И ИЗМЕНЯЕМЫЕ КОРТЕЖИ #

#tuple_ = 1, 2, 3, 4
#tuple_2 = 1, 2, 3, 4
#tuple_3 = tuple ([1, 2, 3, 4])
#print(tuple_)
#print(tuple_2)
#print(tuple_3)
#print(type(tuple_))

tuple_ = 1, 2, 3, True, "тапочек"
list_ = [1, 2, 3, True, "тапочек"]
#print(tuple_[0])
#tuple_[0] = 200      # кортеж не поменяет данные
#print(tuple_.__sizeof__())
#print(list_.__sizeof__())
tuple_ = ([1, 2], 0)
print(tuple_)
tuple_[0][0] = 2
print(tuple_)

tuple_ = ([1, 2], 0) + (3, 7)
print(tuple_)
tuple_[0][0] = 2
print(tuple_)

tuple_ = (4, 7) * 5
print(tuple_)



