import pygame as pg
from Perlin_noize import perlin_noize_octaves


class Ground:
    def __init__(self, world_width, frequencies, amplitudes, seeds, ground_color, ground_constant,
                 ground_damping_constant):
        self.world_width = world_width
        self.curve_points = perlin_noize_octaves(world_width, frequencies, amplitudes, seeds)
        self.curve_points = self.curve_points + 520
        self.ground_height = 2500
        self.surface = pg.Surface((world_width, self.ground_height)).convert_alpha()
        self.ground_color = ground_color
        self.ground_constant = ground_constant
        self.ground_damping_constant = ground_damping_constant

        self.build_ground()

    def build_ground(self):
        self.surface.fill((0, 0, 0, 0))

        points = [(0, self.ground_height)] + \
                 [(x, int(self.curve_points[x])) for x in range(self.world_width)] + \
                 [(self.world_width - 1, self.ground_height)]

        pg.draw.polygon(self.surface, self.ground_color, points)

    def draw(self, screen, camera):
        screen.blit(self.surface, (-camera.x, -camera.y))
