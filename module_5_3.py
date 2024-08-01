class House:
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
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
h2.name = 'ЖК Эльбрус'
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__