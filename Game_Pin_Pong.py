
import arcade

SCREEN_WIDTH = 800                                 ### - ширина окна приложения
SCREEN_HEIGHT = 600                                ### - высота окна приложения
SCREEN_TITLE = "Pong Game"                         ### - название игры

class Boll(arcade.Sprite):
    def __init__(self):
        super().__init__("boll_pong.png", 0.4)    ### - характеристики мяча и его расположение
        self.change_x = 5                                       ### - скорость перемещения мячика по Х
        self.change_y = 5                          ### - скорость перемещения мячика по У
    def update(self):                              ### - описание движения мяча в пространстве
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x = - self.change_x
        if self.left <= 0:
            self.change_x = - self.change_x
        if self.top >= SCREEN_HEIGHT:
            self.change_y = - self.change_y
        if self.bottom <= 0:
            self.change_y = - self.change_y


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__("bar_pong.png", 0.2)     ### - характеристики ракетки и ее расположение

    def update(self):                                           ### - описание движения ракетки в пространстве
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.boll = Boll()
        self.setup()


    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 7
        self.boll.center_x = SCREEN_WIDTH / 2
        self.boll.center_y = SCREEN_HEIGHT / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.boll.draw()
    # pass
    def update(self, delta):

        if arcade.cheсk_for_collision(self.bar, self.boll):   ### - столкновение мяча и ракетки
                                                ### - ОШИБКА - module 'arcade' has no attribute 'cheсk_for_collision'

            self.boll.change_y = - self.boll.change_y      ### - изменение направления движения мяча после столкновения
        self.boll.update()                                   ### - переопределение метода update
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5                            ### - скорость перемещения ракетки
        if key == arcade.key.LEFT:
            self.bar.change_x = - 5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)  ############################## 12.50
    arcade.run()































