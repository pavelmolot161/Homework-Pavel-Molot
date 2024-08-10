
class Horse:
    x_distance = 0                    ### - пройденный путь.
    sound = ('Frrr')                  ### - звук, который издает лошадь

    def run(self, dx):
        Horse.x_distance += dx

class Eagle:
    y_distance = 0                                     ### - высота полёта
    sound = ('I train, eat, sleep, and repeat')        ### - звук, который издаёт орёл(отсылка)
    def fly(self, dy):
        Eagle.y_distance += dy

class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (Horse.x_distance, Eagle.y_distance)

    def voice(self):
        Horse.sound = Eagle.sound   ### - неодходима проверка
        print(self.sound)

        ### Пример работы программы:
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()

# print(Horse.mro())                     ### - [<class '__main__.Horse'>, <class 'object'>]
# print(Eagle.mro())                     ### - [<class '__main__.Eagle'>, <class 'object'>]
# print(Pegasus.mro())                   ### - [<class '__main__.Pegasus'>, <class '__main__.Horse'>,
                                                # <class '__main__.Eagle'>, <class 'object'>]





