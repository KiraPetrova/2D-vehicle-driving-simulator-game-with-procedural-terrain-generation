import pygame as pg


class Menu:
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 background,
                 buttons,
                 label=None,
                 label_pos=None):
        self.pos = (x, y)
        self.background = pg.transform.scale(background, (width, height))
        self.buttons = buttons
        self.is_active = False
        self.label = label
        self.label_pos = label_pos

    def draw(self, screen):
        screen.blit(self.background, self.pos)
        for btn in self.buttons:
            btn.draw(screen)
        if self.label is not None:
            screen.blit(self.label, self.label_pos)

    def update(self, event, entry_menu, main_menu, game, pause_menu, finish_menu, fail_menu):
        for btn in self.buttons:
            btn.update(event, entry_menu, main_menu,  game, pause_menu, finish_menu, fail_menu)
