
### - задание 10_2

from threading import Thread
from time import sleep
class Knight(Thread):                    ### Thread - наследуется из - from threading import Thread
    def __init__(self, name, power):
        super().__init__()               ### - гарантирует, что класс Knight наследует все необходимые свойства и методы
                                          ## от базового класса Thread, обеспечивая корректную работу потока
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        number_of_warriors = 100
        day = 0
        while number_of_warriors > 0:
            number_of_warriors -= self.power
            day += 1
            if number_of_warriors < self.power:
                number_of_warriors = 0
            print(f'{self.name}, сражается {day} день(дня)..., осталось {number_of_warriors} воинов.')
            sleep(1)
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')

    ### - Алгоритм выполнения кода: (по заданию)

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')


    ### - Вывод в консоль:
# Sir Lancelot, на нас напали!
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
# Sir Galahad, на нас напали!
# Sir Galahad, сражается 1 день(дня)..., осталось 80 воинов.
# Sir Galahad, сражается 2 день(дня)..., осталось 60 воинов.
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
# Sir Galahad, сражается 3 день(дня)..., осталось 40 воинов.
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
# Sir Galahad, сражается 4 день(дня)..., осталось 20 воинов.
# Sir Galahad, сражается 5 день(дня)..., осталось 0 воинов.
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
# Sir Galahad одержал победу спустя 5 дней(дня)!
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
# Sir Lancelot одержал победу спустя 10 дней(дня)!
# Все битвы закончились!


'''Вызов super().__init__() в конструкторе Knight делает следующее:

Вызывает конструктор базового класса Thread, который выполняет необходимую инициализацию для объекта потока.
Обеспечивает, что все атрибуты и методы, определенные в Thread, будут доступны в классе Knight.
Это важно, потому что Thread определяет множество важных атрибутов и методов, таких как name, daemon, start(),
run() и др. Если бы мы не вызвали super().__init__(), то эти атрибуты и методы не были бы доступны в классе Knight.
Таким образом, использование super().__init__() гарантирует, что класс Knight наследует все необходимые свойства
и методы от базового класса Thread, обеспечивая корректную работу потока.'''

