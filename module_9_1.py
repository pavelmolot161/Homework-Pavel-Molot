

def apply_all_func(int_list: (int, float), *functions):

    result = {}
        ### - Перебор функций
    for func in functions:
        ### - Вычисляем результат функции и сохраняем в словарь
        result[func.__name__] = func(int_list)    ### - Изучить конструкцию

    return result

        ### - Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


        ### - Вывод на консоль:
# {'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}














