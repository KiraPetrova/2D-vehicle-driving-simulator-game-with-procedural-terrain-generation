import pygame as pg


class Labels:
    def __init__(self):
        self.finish_level = self.render(f"УРОВЕНЬ ПРОЙДЕН!", None, 72, (0, 255, 0))
        self.fail_level = self.render(f"УРОВЕНЬ НЕ ПРОЙДЕН!", None, 72, (255, 0, 0))

    def render(self, text, style, size, color):
        font_object = pg.font.Font(style, size)
        return font_object.render(text, True, color)

    def get_time(self, time_left):
        return self.render(f"{time_left}", None, 72, (255, 20, 147))
