
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner                      ### - владелец транспорта. (владелец может меняться)
        self.__model = __model                  ### - модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power    ### - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = __color                  ### - название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_mode(self):
        return f"Модель: {self.__model}"            ### - вызов через точку

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):

        print(self.get_mode())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, set_color):
        if set_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = set_color
            #print("Цвет успешно изменен на", set_color)
        else:
            print("Нельзя сменить цвет на", set_color)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5               ### - (в седан может поместиться только 5 пассажиров)


        # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

        # Изначальные свойства
vehicle1.print_info()

        # Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

        # Проверяем что поменялось
vehicle1.print_info()



