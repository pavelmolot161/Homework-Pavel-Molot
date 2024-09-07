import random

# from random import choice

     ### Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'
result_1 = list(map(lambda x, y: x == y, first, second))
print(result_1)

     ### По заданию результатом должен быть список совпадения букв в той же позиции:
#[False, True, True, False, False, False, False, False, True, False, False, False, False, False]


     ### Замыкание: ________________________________________________________________________________

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:    ### - записываем в файл и раскодируем Русский
                                                ### - r - read (читать), w - write (запись), a - append (добавлять)
            for item in data_set:
                file.write(str(item) + '\n')

    ### - Для проверки что записано в файле 'example.txt'

        with open(file_name, 'r', encoding='utf-8') as file:     ### Читаем содержимое файла и раскодируем на Русский
            content = file.read()
        print(content)                                           ### Выводим содержимое файла в консоль
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

     ### По заданию должно записатся в 'example.txt'
     # Это строчка
     # ['А', 'это', 'уже', 'число', 5, 'в', 'списке']

    ### Метод __call__: ________________________________________________________________________________

from random import choice
class MysticBall:

    def __init__(self, *words):
        self.words = words                                       ### - self.words - становится кортежем

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

     ### Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное








