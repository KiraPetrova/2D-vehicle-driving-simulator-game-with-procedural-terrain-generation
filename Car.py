import pygame as pg


class Car:
    def __init__(self, left_wheel, right_wheel, body, engine_power, brake_power):
        self.left_wheel = left_wheel
        self.right_wheel = right_wheel
        self.body = body
        self.engine_power = engine_power
        self.brake_power = brake_power
        self.wheel_torque = 0

    def control(self, pressed):
        torque = 0
        if pressed[pg.K_RIGHT]:
            torque = self.engine_power
        elif pressed[pg.K_LEFT]:
            torque = -self.brake_power
        self.wheel_torque = torque

    def update(self, gravity, dt):
        self.left_wheel.add_torque(self.wheel_torque)
        self.right_wheel.add_torque(self.wheel_torque)
        self.left_wheel.update(self.body, gravity, dt)
        self.right_wheel.update(self.body, gravity, dt)
        body_center_x = self.body.pos.x + self.body.width // 2
        half_wheel_base = self.body.wheel_base / 2
        self.left_wheel.pos.x = body_center_x - half_wheel_base
        self.right_wheel.pos.x = body_center_x + half_wheel_base  
        self.body.update(self.left_wheel, self.right_wheel, gravity, dt)

    def draw(self, screen, camera):
        self.left_wheel.draw(screen, camera)
        self.right_wheel.draw(screen, camera)
        self.body.draw(screen, camera)
