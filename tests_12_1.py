
### - tests_12_1.py

from unittest import TestCase

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

#____________________________________________________________________________________________________________

class RunnerTest(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def setUp(self):
        self.runner = Runner('running')
        self.runner_2 = Runner('running_2')
        self.runner_a = Runner('running_a')
        self.runner_b = Runner('running_b')

    def test_walk(self):
        self.runner = Runner('running')                  ### - создается экземпляр класса Runner с аргументом 'running'.
        for _ in range(10):
        # for _ in range(11):                            ### - для проверки работы теста
            self.runner.walk()
        self.assertEqual(self.runner.distance,50)

    def test_run(self):
        self.runner_2 = Runner('running_2')              ### - создается экземпляр класса Runner с аргументом 'running_2'.
        for _ in range(10):
        # for _ in range(11):                            ### - для проверки работы теста
            self.runner_2.run()
        self.assertEqual(self.runner_2.distance, 100)

    def test_challenge(self):
        self.runner_a = Runner('running_a')
        for _ in range(10):
            self.runner_a.run()
        self.runner_b = Runner('running_b')
        for _ in range(10):
            self.runner_b.walk()
        self.assertNotEqual(self.runner_a.distance, self.runner_b.distance, '(running_a) должно быть '
                                                                            'не равно (running_b)')

### - ДОПОЛНИТЕЛЬНЫЕ МАТЕРИАЛЫ
'''Метод assertEqual() из unittest сравнивает значение атрибута distance объекта runner с числом 50.  
Если значения равны, тест проходит успешно; в противном случае тест завершается с ошибкой.  
Это утверждение проверяет, что после 10 вызовов метода walk() общее пройденное расстояние равно 50.'''

'''Метод assertNotEqual() — это функция из библиотеки unittest, которая используется в модульном тестировании 
для проверки неравенства двух значений.
Синтаксис: assertNotEqual(firstValue, secondValue, message).
Параметры:
firstValue: переменная любого типа, которая используется для сравнения функцией.
secondValue: переменная любого типа, которая используется для сравнения функцией.
message: строковое предложение, которое выводится в качестве сообщения при неудачном тестовом случае.
Если оба входных значения не равны, assertNotEqual() вернёт True, в противном случае — False.'''

