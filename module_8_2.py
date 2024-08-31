

def personal_sum(numbers):
    result = 0              ### - сумма чисел
    incorrect_data = 0      ### - количество некоректных данных

    for item in numbers:
        try:
            if isinstance(item, int):
                result += item
                # print(f' я из personal_sum {result}')         ### - проверка работы
            else:
                raise TypeError(f'Некорректный тип данных +++') ### - значение в скобках, для чего - ?
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item} ') ### - {item} >>> вывел все
                    # символы из кортежа поочередно включая запятые и пробелы и это все через команду raise
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        count = 0
        total_sum, incorrect_data = personal_sum(numbers) ### - надо разобратся как работает эта конструкция -СЛОЖНО-
        for item in numbers:                              ### - Проверяем, является ли элемент числом
            if isinstance(item, (int, float)):
                count += 1
        return total_sum / count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')



### - ПРОВЕРКА РАБОТЫ С ЧИСЛАМИ моя
# print(personal_sum([2, 3, 4, 'sdf']))
# print(personal_sum(['a ,d, t, r']))
# print(calculate_average([4, 2, 5]))


### - Пример выполнения программы:
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

### - Вывод на консоль:
# Некорректный тип данных для подсчёта суммы - 1
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 2
# Некорректный тип данных для подсчёта суммы - ,
# Некорректный тип данных для подсчёта суммы -
# Некорректный тип данных для подсчёта суммы - 3
# Результат 1: 0
# Некорректный тип данных для подсчёта суммы - Строка
# Некорректный тип данных для подсчёта суммы - Ещё Строка
# Результат 2: 2.0
# В numbers записан некорректный тип данных
# Результат 3: None
# Результат 4: 26.5

