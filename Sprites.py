import pygame as pg


class Sprites:
    def __init__(self,
                 entry_menu_background,
                 entry_menu_but_start_state,
                 entry_menu_but_start_active,
                 entry_menu_but_start_pressed,

                 main_menu_background,
                 main_menu_but_start_state,
                 main_menu_but_start_active,
                 main_menu_but_start_pressed,
                 main_menu_but_settings_state,
                 main_menu_but_settings_active,
                 main_menu_but_settings_pressed,

                 levels_menu_but_1_locked,
                 levels_menu_but_1_state,
                 levels_menu_but_1_active,
                 levels_menu_but_1_pressed,
                 levels_menu_but_2_locked,
                 levels_menu_but_2_state,
                 levels_menu_but_2_active,
                 levels_menu_but_2_pressed,
                 levels_menu_but_3_locked,
                 levels_menu_but_3_state,
                 levels_menu_but_3_active,
                 levels_menu_but_3_pressed,
                 levels_menu_but_4_locked,
                 levels_menu_but_4_state,
                 levels_menu_but_4_active,
                 levels_menu_but_4_pressed,
                 levels_menu_but_5_locked,
                 levels_menu_but_5_state,
                 levels_menu_but_5_active,
                 levels_menu_but_5_pressed,
                 levels_menu_but_6_locked,
                 levels_menu_but_6_state,
                 levels_menu_but_6_active,
                 levels_menu_but_6_pressed,
                 levels_menu_but_7_locked,
                 levels_menu_but_7_state,
                 levels_menu_but_7_active,
                 levels_menu_but_7_pressed,
                 levels_menu_but_8_locked,
                 levels_menu_but_8_state,
                 levels_menu_but_8_active,
                 levels_menu_but_8_pressed,
                 levels_menu_but_9_locked,
                 levels_menu_but_9_state,
                 levels_menu_but_9_active,
                 levels_menu_but_9_pressed,
                 levels_menu_but_10_locked,
                 levels_menu_but_10_state,
                 levels_menu_but_10_active,
                 levels_menu_but_10_pressed,

                 wheel_sprite,
                 body_sprite,

                 game_pause_menu_background,
                 game_pause_button_state,
                 game_pause_button_active,
                 game_pause_button_pressed,
                 game_resume_button_state,
                 game_resume_button_active,
                 game_resume_button_pressed,
                 game_restart_button_state,
                 game_restart_button_active,
                 game_restart_button_pressed,
                 game_exit_button_state,
                 game_exit_button_active,
                 game_exit_button_pressed,

                 house_1,
                 house_2,
                 house_3,

                 finish_back_to_menu_background,
                 finish_back_to_menu_but_state,
                 finish_back_to_menu_but_active,
                 finish_back_to_menu_but_pressed):

        self.entry_menu_background = self.load(entry_menu_background)
        self.entry_menu_but_start_state = self.load(entry_menu_but_start_state)
        self.entry_menu_but_start_active = self.load(entry_menu_but_start_active)
        self.entry_menu_but_start_pressed = self.load(entry_menu_but_start_pressed)

        self.main_menu_background = self.load(main_menu_background)
        self.main_menu_but_start_state = self.load(main_menu_but_start_state)
        self.main_menu_but_start_active = self.load(main_menu_but_start_active)
        self.main_menu_but_start_pressed = self.load(main_menu_but_start_pressed)
        self.main_menu_but_settings_state = self.load(main_menu_but_settings_state)
        self.main_menu_but_settings_active = self.load(main_menu_but_settings_active)
        self.main_menu_but_settings_pressed = self.load(main_menu_but_settings_pressed)

        self.levels_menu_but_1_locked = self.load(levels_menu_but_1_locked)
        self.levels_menu_but_1_state = self.load(levels_menu_but_1_state)
        self.levels_menu_but_1_active = self.load(levels_menu_but_1_active)
        self.levels_menu_but_1_pressed = self.load(levels_menu_but_1_pressed)
        self.levels_menu_but_2_locked = self.load(levels_menu_but_2_locked)
        self.levels_menu_but_2_state = self.load(levels_menu_but_2_state)
        self.levels_menu_but_2_active = self.load(levels_menu_but_2_active)
        self.levels_menu_but_2_pressed = self.load(levels_menu_but_2_pressed)
        self.levels_menu_but_3_locked = self.load(levels_menu_but_3_locked)
        self.levels_menu_but_3_state = self.load(levels_menu_but_3_state)
        self.levels_menu_but_3_active = self.load(levels_menu_but_3_active)
        self.levels_menu_but_3_pressed = self.load(levels_menu_but_3_pressed)
        self.levels_menu_but_4_locked = self.load(levels_menu_but_4_locked)
        self.levels_menu_but_4_state = self.load(levels_menu_but_4_state)
        self.levels_menu_but_4_active = self.load(levels_menu_but_4_active)
        self.levels_menu_but_4_pressed = self.load(levels_menu_but_4_pressed)
        self.levels_menu_but_5_locked = self.load(levels_menu_but_5_locked)
        self.levels_menu_but_5_state = self.load(levels_menu_but_5_state)
        self.levels_menu_but_5_active = self.load(levels_menu_but_5_active)
        self.levels_menu_but_5_pressed = self.load(levels_menu_but_5_pressed)
        self.levels_menu_but_6_locked = self.load(levels_menu_but_6_locked)
        self.levels_menu_but_6_state = self.load(levels_menu_but_6_state)
        self.levels_menu_but_6_active = self.load(levels_menu_but_6_active)
        self.levels_menu_but_6_pressed = self.load(levels_menu_but_6_pressed)
        self.levels_menu_but_7_locked = self.load(levels_menu_but_7_locked)
        self.levels_menu_but_7_state = self.load(levels_menu_but_7_state)
        self.levels_menu_but_7_active = self.load(levels_menu_but_7_active)
        self.levels_menu_but_7_pressed = self.load(levels_menu_but_7_pressed)
        self.levels_menu_but_8_locked = self.load(levels_menu_but_8_locked)
        self.levels_menu_but_8_state = self.load(levels_menu_but_8_state)
        self.levels_menu_but_8_active = self.load(levels_menu_but_8_active)
        self.levels_menu_but_8_pressed = self.load(levels_menu_but_8_pressed)
        self.levels_menu_but_9_locked = self.load(levels_menu_but_9_locked)
        self.levels_menu_but_9_state = self.load(levels_menu_but_9_state)
        self.levels_menu_but_9_active = self.load(levels_menu_but_9_active)
        self.levels_menu_but_9_pressed = self.load(levels_menu_but_9_pressed)
        self.levels_menu_but_10_locked = self.load(levels_menu_but_10_locked)
        self.levels_menu_but_10_state = self.load(levels_menu_but_10_state)
        self.levels_menu_but_10_active = self.load(levels_menu_but_10_active)
        self.levels_menu_but_10_pressed = self.load(levels_menu_but_10_pressed)

        self.wheel_sprite = self.load(wheel_sprite)
        self.body_sprite = self.load(body_sprite)

        self.game_pause_menu_background = self.load(game_pause_menu_background)
        self.game_pause_button_state = self.load(game_pause_button_state)
        self.game_pause_button_active = self.load(game_pause_button_active)
        self.game_pause_button_pressed = self.load(game_pause_button_pressed)
        self.game_resume_button_state = self.load(game_resume_button_state)
        self.game_resume_button_active = self.load(game_resume_button_active)
        self.game_resume_button_pressed = self.load(game_resume_button_pressed)
        self.game_restart_button_state = self.load(game_restart_button_state)
        self.game_restart_button_active = self.load(game_restart_button_active)
        self.game_restart_button_pressed = self.load(game_restart_button_pressed)
        self.game_exit_button_state = self.load(game_exit_button_state)
        self.game_exit_button_active = self.load(game_exit_button_active)
        self.game_exit_button_pressed = self.load(game_exit_button_pressed)

        house_1 = self.load(house_1)
        house_2 = self.load(house_2)
        house_3 = self.load(house_3)
        self.houses_list = [house_1, house_2, house_3]

        self.finish_back_to_menu_background = self.load(finish_back_to_menu_background)
        self.finish_back_to_menu_but_state = self.load(finish_back_to_menu_but_state)
        self.finish_back_to_menu_but_active = self.load(finish_back_to_menu_but_active)
        self.finish_back_to_menu_but_pressed = self.load(finish_back_to_menu_but_pressed)

    def load(self, name):
        return pg.image.load(f"Sprites/{name}").convert_alpha()
