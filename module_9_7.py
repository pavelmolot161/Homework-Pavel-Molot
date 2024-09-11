
def is_prime(func):
    def wrapper(*args: int):
        result = func(*args)                    ### - Мы вызываем result = func(*args) в функции wrapper, что означает,
                                                ## что мы вызываем sum_three и получаем результат.
        print(result)
        for i in range(2, int(result ** 0.5) + 1):
            if not result % i == 0 or result <= 1:
                return "Простое"
            else:
                return "Составное"
    return wrapper

@is_prime
def sum_three(*args: int):
    return sum(args)



    ### - Пример:
result = sum_three(2, 3, 6)
print(result)

    ### - Результат консоли:
# Простое
# 11

