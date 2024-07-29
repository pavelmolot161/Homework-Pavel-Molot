
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

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
