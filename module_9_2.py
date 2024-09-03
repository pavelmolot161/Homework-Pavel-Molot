

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(second_result)

third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}
                                                                            ### - сработала только конкатенация списков
print(third_result)

# result = [[x * y for x in my_numbers for y in they_numbers if x % 2]]
# result = {x: x ** 2 for x in my_numbers}

     ### Пример выполнения кода:

# print(first_result)
# print(second_result)
# print(third_result)

     ### Вывод на консоль:

# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}








