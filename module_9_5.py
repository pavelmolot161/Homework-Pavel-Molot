
class StepValueError(ValueError):
    pass
'''В данном случае мы просто наследуем класс StepValueError от ValueError и оставляем его пустым с помощью 
оператора pass. Это позволит нам использовать этот класс исключения в нашем коде, когда возникнет ситуация, 
которая требует его применения.
Пользовательские классы исключений, наследующиеся от встроенных классов исключений, позволяют нам более точно и 
понятно обрабатывать ошибки в нашем коде. Это помогает сделать код более структурированным и читаемым'''

class Iterator:

    def __init__(self, start: int, stop, step=1):
        self.start = start                        ### - целое число с которого начинается итерация
        self.step = step                          ### - целое число на котором заканчивается итерация
        self.stop = stop                          ### - шаг с которой совершается итерация
        self.pointer = start            ### - указывает на текущее число в итерации изначально указатель равен start
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start                 ### - установка указателя на старт
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()
        current = self.pointer
        self.pointer += self.step                 ### - Инкремент указателя
        return current                            ### - Возвращаем текущее значение указателя


        ### - Пример выполняемого кода:
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, - 1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()

         ### Вывод на консоль:
# Шаг указан неверно
# -5 -4 -3 -2 -1 0 1
# 6 8 10 12 14
# 5 4 3 2 1









