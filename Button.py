import pygame as pg


class Button:
    def __init__(self, x, y, width, height, name, sprite_state, sprite_active, sprite_pressed,
                 level_manager, locked_sprite=None):
        self.rect = pg.Rect(x, y, width, height)
        self.name = name
        self.sprite_state = pg.transform.scale(sprite_state, (width, height))
        self.sprite_active = pg.transform.scale(sprite_active, (width, height))
        self.sprite_pressed = pg.transform.scale(sprite_pressed, (width, height))
        if locked_sprite:
            self.sprite_locked = pg.transform.scale(locked_sprite, (width, height))
        is_level_button = self.name.startswith("levels_menu")
        if is_level_button:
            level_index = int(self.name.split("_")[-1]) - 1
            unlocked_index = level_manager.last_unlocked_level
            if level_index > unlocked_index:
                self.current_sprite = self.sprite_locked
            else:
                self.current_sprite = self.sprite_state
        else:
            self.current_sprite = self.sprite_state

    def entry_menu_button_start_action(self, now_menu, next_menu):
        now_menu.is_active = False
        next_menu.is_active = True


    def select_level_action(self, game, level_index, main_menu):
        level_manager = game.level_manager
        if level_index <= level_manager.last_unlocked_level:
            level_manager.set_current_level_by_index(level_index)
            game.start_current_level()
            game.is_active = True
            main_menu.is_active = False

    def pause_button_action(self, game, pause_menu):
        game.is_active = False
        pause_menu.is_active = True

    def pause_resume_action(self, game, pause_menu):
        game.is_active = True
        pause_menu.is_active = False

    def pause_restart_action(self, game, pause_menu):
        game.start_current_level()
        pause_menu.is_active = False
        game.is_active = True

    def pause_exit_action(self, game, pause_menu, main_menu):
        game.start_current_level()
        pause_menu.is_active = False
        main_menu.is_active = True
        game.is_active = False

    def finish_to_menu_action(self, main_menu, finish_menu, fail_menu):
        finish_menu.is_active = False
        fail_menu.is_active = False
        main_menu.is_active = True

    def draw(self, screen):
        screen.blit(self.current_sprite, (self.rect.x, self.rect.y))

    def update(self, event, entry_menu, main_menu, game, pause_menu,
               finish_menu, fail_menu):
        mouse_pos = pg.mouse.get_pos()

        is_level_button = self.name.startswith("levels_menu")
        if is_level_button:
            self.level_index = int(self.name.split("_")[-1]) - 1
            unlocked_index = game.level_manager.last_unlocked_level
            if self.level_index > unlocked_index:
                self.current_sprite = self.sprite_locked
                return
            else:
                self.current_sprite = self.sprite_state

        if self.rect.collidepoint(mouse_pos):
            self.current_sprite = self.sprite_active

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if is_level_button:
                    self.current_sprite = self.sprite_pressed
                    self.select_level_action(game, self.level_index, main_menu)
                else:
                    if self.name == "entry_menu_button_start":
                        self.entry_menu_button_start_action(entry_menu, main_menu)
                    if self.name == "pause_button":
                        self.pause_button_action(game, pause_menu)
                    if self.name == "pause_resume":
                        self.pause_resume_action(game, pause_menu)
                    if self.name == "pause_restart":
                        self.pause_restart_action(game, pause_menu)
                    if self.name == "pause_exit":
                        self.pause_exit_action(game, pause_menu, main_menu)
                    if self.name == "finish_to_menu_button":
                        self.finish_to_menu_action(main_menu, finish_menu, fail_menu)
        else:
            if not is_level_button:
                self.current_sprite = self.sprite_state
