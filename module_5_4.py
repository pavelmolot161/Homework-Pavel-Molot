class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number
    def go_to(self,floor):
        self.new_floor = floor
        if self.new_floor <= self.number_of_floors or self.new_floor < 1:
            for i in range(1, self.new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return (f"Название: {self.name} количество этажей:  {self.number_of_floors}")
    def __eq__(self, other):
        # if isinstance(self, House):
            # if isinstance(other, House):
                return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
    def __radd__(self, value):
        if isinstance(value, int):
            return House.__add__(self, value)
    def __iadd__(self, value):
        if isinstance(value, int):
            return House.__add__(self, value)
    def __del__(self):
        print(f'Объект {self.name} снесен, но он останется в истории.')
        # return f'{self.name} - снесен, но он останется в истории.'

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)








# class Example:
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         return object.__new__(cls)
#
#     def __init__(self, first, second, third):
#         print(first)
#         print(second)
#         print(third)
#
# ex = Example('data', second=25, third=3.14)





























