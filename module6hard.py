
import math
class Figure:
    sides_count = 0

    def __init__(self, __sides, __color):
        self.__sides = self.__validate_sides(__sides)
        self.__color = self.__validate_color(__color)
        self.filled = False

    def __validate_sides(self, __sides):
        if self.__is_valid_sides(*__sides):
            return list(__sides)
        else:
            return []

    def __is_valid_sides(self, *__sides):
        if len(__sides) != self.sides_count:
            return False
        for i in __sides:
            if not isinstance(i, int) or i <= 0:
                return False
        return True

    def __validate_color(self, __color):
        if self.__is_valid_color(*__color):
            return list(__color)
        else:
            return [0, 0, 0]

    def __is_valid_color(self, r, g, b):
        return (isinstance(r, int) and 0 <= r <= 255 and
                isinstance(g, int) and 0 <= g <= 255 and
                isinstance(b, int) and 0 <= b <= 255)

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return [r, g, b]
        else:
            return self.__color

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

    # sides_count = 0                             ### - количество сторон
    #
    # def __init__(self, __color, __sides):
    #     self.__sides = list(__sides)                  ### - (список сторон(целые числа))
    #     self.__color = __color                  ### - (список цветов в формате RGB)
    #     self.filled = False                     ### - (закрашенный, bool)
    #
        ## if not self.__is_valid_sides(__sides):      ### - СЛОЖНАЯ КОНСТРУКЦИЯ
        ##     self.__sides = [1] * self.sides_count
    # def get_color(self):
    #     return self.__color                     ### - возвращает список RGB цветов
    #
    # def __is_valid_color(self, r, g, b):
    #     return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
    #
    # def set_color(self, r, g, b):              ### - возвращает список RGB цветов
    #     if self.__is_valid_color(r, g, b):     ### - обращение через self к __is_valid_color
    #         self.__color = [r, g, b]
    # def set_sides(self, *new_sides):
    #     if self.__is_valid_sides(*new_sides):
    #         self.__sides = list(new_sides)
#______________________________________________________________________________________

    # def __validate_sides(self, __sides):
    #     if self.__is_valid_sides(*__sides):
    #         return list(__sides)
    #     else:
    #         return []
    #
    # def __is_valid_sides(self, *__sides):
    #     if len(__sides) != self.sides_count:
    #         return False
    #     for side in __sides:
    #         if not isinstance(side, int) or side <= 0:
    #             return False
    #     return True

    ## def __is_valid_sides(self, *valid_sides):  ### - *sides - приходящие число из создаваемого объекта
    ##     self.valid_sides = valid_sides
    ##     if all(isinstance(valid_sides, int) and Circle.sides_count > 0 for valid_sides in Circle.sides_count): ### - не доработан как вызвать поочередно sides_count каждого класса

    ## def __is_valid_sides(self, __sides):
    ##     return len(__sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in __sides)


    # def get_sides(self):              ### - проверить не точно
    #     return self.__sides
    #
    # def __len__(self):
    #     return sum(self.__sides)
    ## def __len__(self):
    ##     return [1] * self.sides_count          ### _ количество сторон фигур


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides, __radius):
        super().__init__(__color, round(2 * math.pi * __radius))
        self.__radius = __radius                ### - рассчитать исходя из длины окружности (одной единственной стороны)

    def get_square(self):                       ### - возвращает площадь круга
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    ## __base = 1
    def __init__(self, __color, *__sides, __height):
        super().__init__(__color, *__sides)
        self.__height = __height

    def __calculate_height(self):
        a, b, c = self.__sides
        s = (a + b + c) / 2
        return 2 * math.sqrt(s * (s - a) * (s - b) * (s - c)) / a

    def get_square(self):
        return 0.5 * self.__sides[0] * self.__height

class Cube(Figure):
    sides_count = 12
    __base_a = 1
    __sides = 12
    def __init__(self, __color, __sides, side_length):
        super().__init__(__color, [side_length] * self.sides_count)

    def get_volume(self):
        return self.__sides[0] ** 3





        ### Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

   ### Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

   ### Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

   ### Проверка периметра (круга), это и есть длина:
print(len(circle1))

   ### Проверка объёма (куба):
print(cube1.get_volume())



   #####Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216                                    ###  7.43






### - if self.__is_valid_color(r, g, b): надо разобратся как работает такой метод обращения















