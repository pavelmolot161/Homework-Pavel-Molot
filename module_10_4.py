import random
from threading import Thread, Lock
from time import sleep
from queue import Queue  ### - Модуль queue реализует очереди с несколькими производителями и несколькими потребителями.

class Table:

    def __init__(self, number: int):
        self.number = number                   ### - номер стола
        self.guest = None                      ### - гость, который сидит за этим столом (по умолчанию None)
class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name                       ### - имя гостя.

    def run(self):
        # rand_num = random.randint(50, 500)   ### - запасной вариант через переменную
        sleep(random.randint(3, 10))     ### - ожидание случайным образом от 3 до 10 секунд.
class Cafe:

    def __init__(self, *tables):
        self.queue = Queue()                   ### - Очередь — это структура данных, которая позволяет добавлять
                                                 # элементы (в данном случае гостей) и извлекать
                                                 # их в порядке, в котором они были добавлены.
        self.tables = list(tables)             ### - присваевается список
        self.lock = Lock()                     ### - блокировка для потокобезопастности

    def guest_arrival(self, *guests):
        for guest in guests:
            free_table = next((table for table in self.tables if table.guest is None), None)
                                               ### - Функция next() в Python возвращает следующий элемент из итератора.
                                                ## Если итератор исчерпан, функция next() возвращает значение по
                                                 # умолчанию, переданное в качестве аргумента.
                                                 # Если параметр по умолчанию опущен и итератор исчерпан,
                                                 # возникает исключение StopIteration.
            if free_table:                ### - если есть свободный стол
                free_table.guest = guest  ### - присваиваем гостя столу
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:

                self.queue.put(guest)     ### - в противном случае помещаем гостя в очередь
                                            # Метод put добавляет элемент (гостя) в конец очереди.
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
                                    ### - empty() — это метод класса Queue, который проверяет, пустая ли очередь.
                                    ## - any() в Python возвращает логическое значение:
                                    # True, если хотя бы один элемент итерации имеет значение
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():  # Если гость закончил есть
                                    ## is_alive() - это метод в Python, который проверяет, жив ли поток, и возвращает
                                    # логическое значение на основе его статуса.
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла).')
                    print(f'Стол номер {table.number} свободен.')
                    table.guest = None  # Освобождаем стол

                    if not self.queue.empty():  ### - # Если очередь не пуста, добавляем гостя с очереди за стол
                        next_guest = self.queue.get()  # Получаем следующего гостя из очереди
                                ### - get() в Python позволяет вернуть значение словаря по ключу, если оно существует,
                                # или другое значение, если указано (по умолчанию возвращает None).
                        table.guest = next_guest  # Садим его за стол
                        next_guest.start()  # Запускаем поток нового гостя
                        print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.')

            # sleep(1)  # Задержка для имитации времени обслуживания

    # Создание столов
tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
    # Создание гостей
guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
cafe = Cafe(*tables)
    # Приём гостей
cafe.guest_arrival(*guests)
    # Обслуживание гостей
cafe.discuss_guests()


# Вывод на консоль (последовательность может меняться из-за случайного время пребывания гостя):
                                        # Maria сел(-а) за стол номер 1
                                        # Oleg сел(-а) за стол номер 2
                                        # Vakhtang сел(-а) за стол номер 3
                                        # Sergey сел(-а) за стол номер 4
                                        # Darya сел(-а) за стол номер 5
                                        # Arman в очереди
                                        # Vitoria в очереди
                                        # Nikita в очереди
                                        # Galina в очереди
                                        # Pavel в очереди
                                        # Ilya в очереди
                                        # Alexandra в очереди
                                        # Oleg покушал(-а) и ушёл(ушла)
                                        # Стол номер 2 свободен
                                        # Arman вышел(-ла) из очереди и сел(-а) за стол номер 2
                                        # .....
                                        # Alexandra покушал(-а) и ушёл(ушла)
                                        # Стол номер 4 свободен
                                        # Pavel покушал(-а) и ушёл(ушла)
                                        # Стол номер 3 свободен
#














