
### - модуль 10.3

import random
from time import sleep
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0                         ### - Начальный баланс
        self.lock = Lock()                       ### - Создаем объект Lock

    def deposit(self):
        for _ in range(100):                                          ### - 100 транзакций пополнения
            random_number = random.randint(50, 500)
            self.lock.acquire()                                       ### - Открываем замок перед увеличением баланса
            try:
                if self.balance >= 500:                               ### - Пропускаем итерацию, если баланс уже >= 500
                    continue
                self.balance += random_number
                if self.balance >= 500:                               ### - Пропускаем итерацию, если баланс уже >= 500
                    continue
                else:
                    print(f'Пополнение: {random_number}. Баланс: {self.balance}.')
                sleep(0.001)                                          ### - Имитация задержки (нужна или нет - ?)
            finally:
                self.lock.release()                               ### - Освобождаем замок в любом случае

    def take(self):
        for _ in range(100):                                      ### - 100 транзакций снятия
            random_number2 = random.randint(50, 500)
            print(f'Запрос на {random_number2}.')
            self.lock.acquire()                                   ### - Блокируем поток
            try:
                if random_number2 <= self.balance:
                    self.balance -= random_number2
                    print(f'Снятие: {random_number2}. Баланс: {self.balance}.')
                else:
                    print("Запрос отклонён, недостаточно средств.")
            finally:
                self.lock.release()                               ### - Освобождаем замок в любом случае
            sleep(0.001)                                          ### - Имитация задержки (для чего - ?)


# Создаем объект класса Bank
bk = Bank()

# Создаем потоки для методов deposit и take

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ждем завершения потоков
th1.join()
th2.join()

# Выводим итоговый баланс
print(f'Итоговый баланс: {bk.balance}.')

        ### - Вывод на консоль (может отличаться значениями, логика должна быть та же):
# Пополнение: 241. Баланс: 241
# Запрос на 174
# Снятие: 174. Баланс: 67
# Пополнение: 226. Баланс: 293
# Запрос на 421
# Запрос отклонён, недостаточно средств
# Пополнение: 133. Баланс: 426
# Запрос на 422
# Снятие: 422. Баланс: 4
# Пополнение: 150. Баланс: 154
# Запрос на 207
# Запрос отклонён, недостаточно средств
# ....
# Запрос на 431
# Снятие: 431. Баланс: 276
# Запрос на 288
# Запрос отклонён, недостаточно средств
# Итоговый баланс: 276
