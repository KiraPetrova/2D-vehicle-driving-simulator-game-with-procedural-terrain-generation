import random
import pygame as pg


class House:
    def __init__(self, x, y, width, height, houses_list):
        self.rect = pg.Rect(x, y, width, height)
        house_sprite = random.choice(houses_list)
        self.house_sprite = pg.transform.scale(house_sprite, (width, height))

    def draw(self, screen, camera):
        x = self.rect.x - camera.x
        y = self.rect.y - camera.y
        screen.blit(self.house_sprite, (x, y))
