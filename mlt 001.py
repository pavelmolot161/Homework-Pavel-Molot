
   # СТРОКИ И ИНДЕКСАЦИЯ  СТРОК #

# name = 'Павел'
# print("Привет, " + name)

# name = 'Павел'
# print("Привет, " "Павел")

# name = 'Павел'
# print("Привет, " + "Павел")

# print("Привет, " * 6)

# name = "Павел"
# print(name[0])
#
# name = "Павел"
# print(name[-1])
#
# name = "Павел"
# print(name[0:3])
#
# name = "Павел"
# print(name[0:3:2])
#
# name = "Павел"
# print(name[:3]) # тоже самое, как без "0"
#
# name = "Павел"
# print(name[3:])
#
# name = "Павел"
# print(name[::-1]) # Имя наоборот

   # ДЗ СТРОКИ И ИНДЕКСАЦИЯ  СТРОК #

# exampl = 'Топинамбур'
# print(exampl)
# print(exampl[0])
# print(exampl[-1])
# print(exampl[5:])
# print(exampl[::-1])
# print(exampl[0:10:2])   # Тпнму
# print(exampl[1:10:2])   # оиабр из домашки

#########################################################

   # БАЗОВЫЕ СТРУКТУРЫ ДАННЫХ #

# print(5)
# print(type(5)) # int - целое число
#
# print(5 + 5)
# print(5 - 5)
# print(5 * 5)
# print(5 / 5)
# print(5 // 5)
# print(9 % 5)
# print(5 ** 5)
# print(2.0)
# print(type(2.0))
# print(2.2 + 4.6)

# print('Здравствуй, Русский Мир !!!')
# print(type('Здравствуй, Русский Мир !!!')) # string - строка
#
# print("Здравствуй, 'Русский Мир !!!'")
# print(type('Здравствуй, Русский Мир !!!')) # string - строка
#
# print('Здравствуй,' + ' Мир !!!')

# print('1' + 1) # TypeError: can only concatenate str (not "int") to str

# print('1' + '1')

# print(type(True), type(False)) # <class 'bool'> <class 'bool'>
#
# print(5 > 10) # False
# print(5 > 10, 5 < 10) # False True
# print(1, 2, 3, 4, 'Автобус', (5 < 10)) # 1 2 3 4 Автобус True
# print(5<=5, 6<=5, 6>+5, 11>=11) # True False True True
# print(5==5, 6!=5, 6==5, 11!=11) # True True False False
#
# print(5 != 5 and 5 < 11) # False
# print(5 == 5 or 5 < 11) # True
# print(5 != 5 or 5 < 11) # True
# print(5 != 5 or 5 > 11) # False

#     # как перевести строковое данное в цифровое и наоборот
# print(type(int('5'))) # <class 'int'>
# print(type(str(5))) # <class 'str'>

# ДЗ "БАЗОВЫЕ СТРУКТУРЫ ДАННЫХ"

# a = 'Привет моя семья'
# print(len(a))
# first = (4+6)
# second = (15-12)
# summa = first
# diff = second
# print(summa)
# print(diff)
# mean = (5, 7, 22)
# d = sum(mean) / len(mean)
# print(d)                     # 11.333333333333334
# first_string = 'Понедельник, '
# second_string = 'Вторник'
# g = first_string + second_string
# print(g)                     # Понедельник, Вторник
# a = 4
# b = 2
# c = 3
# f = (((a * d) + (a * c)) ** 3) / 2
# print(f)                     # 94230.51851851853

####################################################

   # ПЕРЕМЕННЫЕ #

# name = 'Переменная'
# print(name)
# name = 'Автобус'
# print(name)

# date_of_berth = "Март 2022"
# dateOFBerth = "Март 2022"
#
   # ДЗ ПЕРЕМЕННЫЕ #
#
# name_1 = 'всего задач:'
# name_2 = '12,'
# name_3 = 'затрачено часов:'
# name_4 = '1.5,'
# name_5 = 'среднее время выполнения'
# name_6 = '0.125'
# print('Курс: Python,', name_1, name_2, name_3,
#       name_4, name_5, name_6, 'часа.')

##########################################################

   # ДИНАМИЧЕСКАЯ ПОЗИЦИЯ #

# name = 'Арбуз'
# print(name,type(name)) # Арбуз <class 'str'>
# name = 6
# print(name,type(name)) # 6 <class 'int'>
# name = 5.5
# print(name,type(name)) # 5.5 <class 'float'>
# name = [1, 3, 5]
# print(name,type(name))  # [1, 3, 5] <class 'list'>
#
# age = 30
# new_age = '30'
# print(age + new_age) # ОШИБКА TypeError: unsupported
   # operand type(s) for +: 'int' and 'str'

   # ДЗ "3" ДИНАМИЧЕСКАЯ ТИПИЗАЦИЯ #

# name = 'Pavel'
# print(name)
# age = 41
# print(age)
# age = 40
# print(age)
# is_student = True
# print(is_student)

############################################################

   # ПОТОК ВЫПОЛНЕНИЯ ПРОГРАММЫ, КАК ИНТЕРПРИТАТОР ПОКАЗЫВАЕТ ПЕРЕМЕННЫЕ #

# from time import sleep
#
# a = 5
# print(a)
# print('Я тут')
# sleep(4)
# print('Ну вот, 4 секунды прошло')
#
   # ДЗ  ПОТОК ВЫПОЛНЕНИЯ ПРОГРАММЫ #
#
# print('Hi, PyCharm')
# x = 43
# y = 32
# print(x * y)
# print("End Line")

##################################################

   # организация программ и методы строк #
#
# name = input('Введите Ваше имя: ')
# print(type(name))

# name = input('Введите Ваше имя: ')
# print("Здравствуйту, ", name)

# name = input('Введите Ваше имя: ')
# current_year = 2024
# date_of_birth = int(input("В каком году Вы родились ? "))
# asd = current_year - date_of_birth
# print("Здравствуйте, ", name)
# print("В этом году вам ", asd, "годa")

# print('Привет я строка в нижнем регистре'.upper())
# print('Привет я строка в нижнем регистре'.lower())
# print('Привет я строка в '
#       'нижнем регистре'.replace('Привет', 'Пока'))

print('Привет я строка в '
      'нижнем регистре'.replace(' ', '@'))
























































































