class House:
    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number
    def go_to(self,floor):
        self.new_floor = floor
        for i in range(1, self.new_floor + 1):
            if self.new_floor <= self.number_of_floors or self.new_floor < 1:
                print(i)
            else:
                print("Такого этажа не существует")
                break
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название: {self.name} количество этажей:  {self.number_of_floors}")

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))