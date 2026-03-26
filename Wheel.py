import math

import pygame as pg


class Wheel:
    def __init__(self, center, radius, color, ground, wheel_sprite):
        self.pos = pg.Vector2(center[0], center[1])
        self.velocity = pg.Vector2(0, 0)
        self.radius = radius
        self.mas = 40
        self.spring_constant = 15000
        self.spring_damping_constant = 2000
        self.color = color
        self.ground = ground
        self.wheel_sprite = pg.transform.scale(wheel_sprite, (radius * 2, radius * 2))
        self.rest_length = None
        self.angular_velocity = 0
        self.torque = 0
        self.current_angle = 0
        self.I = 0.5 * self.mas * radius ** 2
        self.max_velocity = 1000

    def vertical_spring_force(self, body):
        current_length = (body.pos.y + body.height / 2) - self.pos.y
        displacement = current_length - self.rest_length
        k = self.spring_constant
        return -k * displacement

    def vertical_damping_force(self, body):
        c = self.spring_damping_constant
        return -c * (body.velocity.y - self.velocity.y)

    def vertical_suspension_force(self, body):
        force = self.vertical_spring_force(body) + self.vertical_damping_force(body)
        return force

    def ground_spring_force(self, entering):
        k = self.ground.ground_constant
        return -k * entering

    def ground_damping_force(self):
        c = self.ground.ground_damping_constant
        return -c * self.velocity.y

    def ground_force(self, entering):
        force = self.ground_spring_force(entering) + self.ground_damping_force()
        return force

    def on_the_ground(self, dt):
        ground_y = self.ground.curve_points[int(self.pos.x)]
        entering = (self.pos.y + self.radius) - ground_y
        if entering > 0:
            F = self.ground_force(entering)
            self.velocity.y += (F / self.mas) * dt
            return True
        else:
            return False

    def gravity_force(self, gravity):
        return self.mas * gravity

    def add_torque(self, tau):
        self.torque += tau

    def apply_drive(self, dt):
        tau_total = self.torque

        if self.angular_velocity > 0:
            passive_brake = -100000
        else:
            passive_brake = 100000
        tau_total += passive_brake

        self.angular_velocity += (tau_total / self.I) * dt
        self.angular_velocity = max(min(self.angular_velocity, self.max_velocity), -self.max_velocity)
        self.torque = 0

    def get_angle(self, dt):
        self.current_angle += math.degrees(self.angular_velocity * dt)
        self.current_angle %= 360

    def update(self, body, gravity, dt):
        self.apply_drive(dt)
        self.get_angle(dt)
        F_total = -self.vertical_suspension_force(body) + self.gravity_force(gravity)
        self.velocity.y += (F_total / self.mas) * dt
        self.velocity.y = max(min(self.velocity.y, self.max_velocity), -self.max_velocity)
        self.is_touching_ground = self.on_the_ground(dt)
        self.pos.y += self.velocity.y * dt

    def draw(self, screen, camera):
        x = self.pos.x - camera.x
        y = self.pos.y - camera.y
        rotated_image = pg.transform.rotate(self.wheel_sprite, -self.current_angle)
        rect = rotated_image.get_rect(center=(x, y))
        screen.blit(rotated_image, rect.topleft)
