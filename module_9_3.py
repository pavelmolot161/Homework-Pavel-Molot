
   ### - module_9_3

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

   ### - генератор для вычисления разности символов
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))
   ### - Пример выполнения кода:

print(list(first_result))
print(list(second_result))

   ### Вывод в консоль:

# [1, 2]
# [False, False, True]




