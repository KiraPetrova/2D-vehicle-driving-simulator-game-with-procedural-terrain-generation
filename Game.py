from Wheel import *
from Body import *
from Car import *
from House import *
from Labels import *


class Game:
    def __init__(self,
                 wheel_sprite,
                 body_sprite,
                 pause_button,
                 level_manager,
                 sprites,
                 camera,
                 labels):

        self.pause_button = pause_button
        self.wheel_sprite = wheel_sprite
        self.body_sprite = body_sprite
        self.level_manager = level_manager
        self.sprites = sprites
        self.camera = camera
        self.labels = labels
        self.is_active = False

    def start_current_level(self):
        level = self.level_manager.get_current_level()
        self.camera.update_world_width(level.world_width)

        self.gravity = level.gravity
        self.time = level.time
        self.time_left = self.time
        self.ground = self.level_manager.grounds[self.level_manager.current_level_index]
        self.house = House(level.world_width - 200, self.ground.curve_points[-200] - 300, 400, 400,
                           self.sprites.houses_list)
        self.background_color=level.background_color

        self.setup_car()

    def setup_car(self):
        ground = self.ground

        self.body = Body(150, 180, 160, 120, (255, 0, 0), ground, self.body_sprite)
        self.left_wheel = Wheel((80, 260), 23, (0, 0, 0), ground, self.wheel_sprite)
        self.right_wheel = Wheel((190, 260), 23, (0, 0, 0), ground, self.wheel_sprite)
        self.car = Car(self.left_wheel, self.right_wheel, self.body, 200000, 200000)

        # вычисляем длину покоя подвески
        self.left_wheel.rest_length = (self.body.pos.y + self.body.height / 2) - self.left_wheel.pos.y-55
        self.right_wheel.rest_length = (self.body.pos.y + self.body.height / 2) - self.right_wheel.pos.y-55

    def update(self, dt, finish_menu, fail_menu):
        self.the_end(finish_menu)
        self.update_timer(dt, fail_menu)
        pressed = pg.key.get_pressed()
        self.car.control(pressed)
        self.car.update(self.gravity, dt)
        self.camera.current(self.body.pos)

    def update_timer(self, dt, fail_menu):
        self.time_left -= dt
        if self.time_left <= 0:
            self.show_fail_menu(fail_menu)

    def show_fail_menu(self, fail_menu):
        self.is_active = False
        fail_menu.is_active = True

    def the_end(self, finish_menu):
        if self.body.rect.colliderect(self.house.rect):
            self.is_active = False
            finish_menu.is_active = True

            self.level_manager.save_progress(self.level_manager.current_level_index)
            self.level_manager.next_level()

    def draw(self, screen):
        screen.fill(self.background_color)

        self.ground.draw(screen, self.camera)
        self.car.draw(screen, self.camera)
        self.pause_button.draw(screen)
        self.house.draw(screen, self.camera)

        time_label = self.labels.get_time(int(self.time_left))
        screen.blit(time_label, (30, 30))
