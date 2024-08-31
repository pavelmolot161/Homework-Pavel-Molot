
def add_everything_up(a, b):
    try:
        d = (a + b)
        return f"{round(d, 3)}"
    except TypeError:
        return f"{str(a)}{str(b)}"


        ### - ПРОВЕРКА ЧИСЛА
# print(add_everything_up(3, 2))

        ###   ПРИМЕР КОДА:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))


        ### - Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456

# return f"{round(d, 3)}"     ### - округляет число после запятой на указанное количество знаков