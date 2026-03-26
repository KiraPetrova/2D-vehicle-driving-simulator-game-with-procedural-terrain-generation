import pygame as pg
import math


class Body:
    def __init__(self, x, y, width, height, color, ground, body_sprite):
        self.rect = pg.Rect(x, y, width, height)
        self.pos = pg.Vector2(x, y)
        self.width = width
        self.height = height
        self.velocity = pg.Vector2(0, 0)
        self.mas = 300
        self.color = color
        self.ground = ground
        self.body_sprite = pg.transform.scale(body_sprite, (width, height))
        self.wheel_base = self.width // 2 + 10
        self.angle = 0
        self.angular_velocity = 0
        self.angular_damping_const = 40000000
        self.angular_stiffness_const = 400000000
        self.I = 1 / 12 * self.mas * (width ** 2 + height ** 2)
        self.max_velocity = 1000

    def gravity_force(self, gravity):
        return self.mas * gravity

    def angular_spring_moment(self, left_wheel, right_wheel):
        dy = right_wheel.pos.y - left_wheel.pos.y
        dx = self.wheel_base
        target_angle = math.atan2(dy, dx)  # который нужен
        angular_displacement = self.angle - target_angle
        k = self.angular_stiffness_const
        return -k * angular_displacement

    def angular_damping_moment(self):
        c = self.angular_damping_const
        return -c * self.angular_velocity

    def angular_suspension_moment(self, left_wheel, right_wheel):
        force = self.angular_spring_moment(left_wheel, right_wheel) + self.angular_damping_moment()
        return force

    def update_horizontal_motion(self, left_wheel, right_wheel, dt):
        wheel_speed_x = (left_wheel.angular_velocity + right_wheel.angular_velocity) / 2 * left_wheel.radius

        if left_wheel.is_touching_ground or right_wheel.is_touching_ground:
            self.velocity.x = wheel_speed_x

        self.pos.x += self.velocity.x * dt

        if self.pos.x < 0:
            self.pos.x = 0
            self.velocity.x = 0

        elif self.pos.x + self.width > len(self.ground.curve_points):
            self.pos.x = len(self.ground.curve_points) - self.width
            self.velocity.x = 0

    def update_vertical_motion(self, left_wheel, right_wheel, gravity, dt):
        F_total = self.gravity_force(gravity)
        F_total += left_wheel.vertical_suspension_force(self)
        F_total += right_wheel.vertical_suspension_force(self)
        self.velocity.y += (F_total / self.mas) * dt
        self.velocity.y = max(min(self.velocity.y, self.max_velocity), -self.max_velocity)
        self.pos.y += self.velocity.y * dt

    def update_angular_motion(self, left_wheel, right_wheel, dt):
        self.angular_velocity += (self.angular_suspension_moment(left_wheel, right_wheel) / self.I) * dt
        self.angle += self.angular_velocity * dt

    def update(self, left_wheel, right_wheel, gravity, dt):
        self.update_vertical_motion(left_wheel, right_wheel, gravity, dt)
        self.update_angular_motion(left_wheel, right_wheel, dt)
        self.update_horizontal_motion(left_wheel, right_wheel, dt)
        self.rect.topleft = (self.pos.x, self.pos.y)

    def draw(self, screen, camera):
        x = self.pos.x - camera.x
        y = self.pos.y - camera.y
        x = x + self.width / 2
        y = y + self.height / 2
        rotated = pg.transform.rotate(self.body_sprite, -math.degrees(self.angle))
        rect = rotated.get_rect(center=(x, y))
        screen.blit(rotated, rect.topleft)
