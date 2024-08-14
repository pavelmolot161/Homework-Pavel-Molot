
import math
class Figure:
    sides_count = 0                                         ### - количество сторон

    def __init__(self, __sides, __color):                   ### - (список сторон (целые числа))
        self.__sides = self.__validate_sides(__sides)       ### - (список цветов в формате RGB)
        self.__color = self.__validate_color(__color)       ### - (закрашенный, bool)
        self.filled = False

    def __validate_sides(self, __sides):                    ### - вспомогательный
        if isinstance(__sides, int):
            return [__sides]
        if self.__is_valid_sides(*__sides):
            return list(__sides)
        else:
            return []

    def __is_valid_sides(self, *__sides):                    ### - служебный, принимает неограниченное кол-во сторон
        if len(__sides) != self.sides_count:
            return False
        for i in __sides:
            if not isinstance(i, int) or i <= 0:
                return False
        return True

    def __validate_color(self, __color):
        validate_list = []
        for color_item in __color:
            validate_list.append(color_item)
        if self.__is_valid_color(*validate_list):
            return list(__color)
        else:
            return [0, 0, 0]

    def __is_valid_color(self, r, g, b):                      ### - служебный, принимает параметры r, g, b
        return (isinstance(r, int) and 0 <= r <= 255 and
                isinstance(g, int) and 0 <= g <= 255 and
                isinstance(b, int) and 0 <= b <= 255)

    def get_color(self):                                      ### - возвращает список RGB цветов
        return self.__color

    def set_color(self, r, g, b):                ### - принимает параметры r, g, b - числа и изменяет атрибут __color
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            return [r, g, b]
        else:
            return self.__color

    def get_sides(self):                          ### - должен возвращать значение я атрибута __sides.
        return self.__sides

    def set_sides(self, *new_sides):              ### - должен принимать новые стороны, если их количество не равно
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):                            ### - должен возвращать периметр фигуры.
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, __sides):
        super().__init__(__sides, __color)
        self.__radius = 0                       

    def get_square(self):                       ### - возвращает площадь круга
        return math.pi * self.__radius ** 2     ### - расчет площади круга

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
    def __init__(self, __color, __sides):
        array = []
        for _ in range(self.sides_count):
            array.append(__sides)

        cube_sides = [__sides for _ in range(self.sides_count)]
        super().__init__(cube_sides, __color)
        self.__sides = cube_sides

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
















