

class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(vin)                                        ### - вызов функции в ините
        self.__is_valid_numbers(numbers)                                ### - вызов функции в ините

    def __is_valid_vin(self, vin_number):
        # self.vin_number = vin_number                                  ### - почему не нужен селф
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')

        if vin_number not in range(1000000, 9999999 + 1):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        # self.numbers = numbers                                        ### - почему не нужен селф
        if not isinstance(numbers, str):                                ### - если значение не строковое то
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')

        if len(self.__numbers) != 6:                                    ### - если количество элементов не равно 6
            raise IncorrectCarNumbers('Неверная длина номера')

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

     ### - Пример выполняемого кода:
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')


      ### - Вывод на консоль:
# Model1 успешно создан
# Неверный диапазон для vin номера
# Неверная длина номера


