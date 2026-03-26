import sys
from Sprites import *
from Camera import *
from Button import *
from Menu import *
from Game import *
from Level_manager import *
from Labels import *

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((1280, 720))

sprites = Sprites(
    'entry_menu_background.png',
    'entry_menu_but_start_state.png',
    'entry_menu_but_start_active.png',
    'entry_menu_but_start_pressed.png',

    'main_menu_background.png',
    'main_menu_but_start_state.png',
    'main_menu_but_start_active.png',
    'main_menu_but_start_pressed.png',
    'main_menu_but_settings_state.png',
    'main_menu_but_settings_active.png',
    'main_menu_but_settings_pressed.png',

    'levels_menu_but_1_locked.png',
    'levels_menu_but_1_state.png',
    'levels_menu_but_1_active.png',
    'levels_menu_but_1_pressed.png',
    'levels_menu_but_2_locked.png',
    'levels_menu_but_2_state.png',
    'levels_menu_but_2_active.png',
    'levels_menu_but_2_pressed.png',
    'levels_menu_but_3_locked.png',
    'levels_menu_but_3_state.png',
    'levels_menu_but_3_active.png',
    'levels_menu_but_3_pressed.png',
    'levels_menu_but_4_locked.png',
    'levels_menu_but_4_state.png',
    'levels_menu_but_4_active.png',
    'levels_menu_but_4_pressed.png',
    'levels_menu_but_5_locked.png',
    'levels_menu_but_5_state.png',
    'levels_menu_but_5_active.png',
    'levels_menu_but_5_pressed.png',
    'levels_menu_but_6_locked.png',
    'levels_menu_but_6_state.png',
    'levels_menu_but_6_active.png',
    'levels_menu_but_6_pressed.png',
    'levels_menu_but_7_locked.png',
    'levels_menu_but_7_state.png',
    'levels_menu_but_7_active.png',
    'levels_menu_but_7_pressed.png',
    'levels_menu_but_8_locked.png',
    'levels_menu_but_8_state.png',
    'levels_menu_but_8_active.png',
    'levels_menu_but_8_pressed.png',
    'levels_menu_but_9_locked.png',
    'levels_menu_but_9_state.png',
    'levels_menu_but_9_active.png',
    'levels_menu_but_9_pressed.png',
    'levels_menu_but_10_locked.png',
    'levels_menu_but_10_state.png',
    'levels_menu_but_10_active.png',
    'levels_menu_but_10_pressed.png',

    'wheel_sprite.png',
    'body_sprite.png',

    'game_pause_menu_background.png',
    'game_pause_button_state.png',
    'game_pause_button_active.png',
    'game_pause_button_pressed.png',
    'game_resume_button_state.png',
    'game_resume_button_active.png',
    'game_resume_button_pressed.png',
    'game_restart_button_state.png',
    'game_restart_button_active.png',
    'game_restart_button_pressed.png',
    'game_exit_button_state.png',
    'game_exit_button_active.png',
    'game_exit_button_pressed.png',

    'house_1.png',
    'house_2.png',
    'house_3.png',

    'finish_back_to_menu_background.png',
    'finish_back_to_menu_but_state.png',
    'finish_back_to_menu_but_active.png',
    'finish_back_to_menu_but_pressed.png'
)

labels = Labels()

level_manager = Level_manager(sprites)
current_level = level_manager.get_current_level()

menus = []

entry_menu_buttons = []
entry_menu_button_start = Button(screen.get_width() // 2 - 300 / 2, screen.get_height() // 2 - 200 / 2, 300, 200,
                                 "entry_menu_button_start",
                                 sprites.entry_menu_but_start_state,
                                 sprites.entry_menu_but_start_active,
                                 sprites.entry_menu_but_start_pressed,
                                 level_manager)
entry_menu_buttons.append(entry_menu_button_start)

entry_menu = Menu(0, 0, screen.get_width(), screen.get_height(), sprites.entry_menu_background, entry_menu_buttons)
menus.append(entry_menu)

main_menu_buttons = []

levels_menu_but_1 = Button(
    300, 200,
    120, 120,
    "levels_menu_but_1",
    sprites.levels_menu_but_1_state,
    sprites.levels_menu_but_1_active,
    sprites.levels_menu_but_1_pressed,
    level_manager,
    sprites.levels_menu_but_1_locked
)
main_menu_buttons.append(levels_menu_but_1)

levels_menu_but_2 = Button(
    500, 200,
    120, 120,
    "levels_menu_but_2",
    sprites.levels_menu_but_2_state,
    sprites.levels_menu_but_2_active,
    sprites.levels_menu_but_2_pressed,
    level_manager,
    sprites.levels_menu_but_2_locked
)
main_menu_buttons.append(levels_menu_but_2)

levels_menu_but_3 = Button(
    700, 200,
    120, 120,
    "levels_menu_but_3",
    sprites.levels_menu_but_3_state,
    sprites.levels_menu_but_3_active,
    sprites.levels_menu_but_3_pressed,
    level_manager,
    sprites.levels_menu_but_3_locked
)
main_menu_buttons.append(levels_menu_but_3)

main_menu = Menu(
    0, 0,
    screen.get_width(), screen.get_height(),
    sprites.main_menu_background,
    main_menu_buttons
)

menus.append(main_menu)

finish_buttons = []

finish_to_menu_button = Button(
    screen.get_width() // 2 - 400 // 2, screen.get_height() // 2 - 400 // 2,
    400, 400,
    "finish_to_menu_button",
    sprites.finish_back_to_menu_but_state,
    sprites.finish_back_to_menu_but_active,
    sprites.finish_back_to_menu_but_pressed,
    level_manager
)

finish_buttons.append(finish_to_menu_button)

finish_menu = Menu(
    0, 0,
    screen.get_width(), screen.get_height(),
    sprites.finish_back_to_menu_background,
    finish_buttons,
    labels.finish_level,
    (screen.get_width() // 2 - 200, 100)
)

menus.append(finish_menu)

fail_buttons = []

fail_buttons.append(finish_to_menu_button)

fail_menu = Menu(
    0, 0,
    screen.get_width(), screen.get_height(),
    sprites.finish_back_to_menu_background,
    finish_buttons,
    labels.fail_level,
    (screen.get_width() // 2 - 200, 100)
)

menus.append(fail_menu)

pause_buttons = []

button_resume = Button(980, 120, 150, 150,
                       "pause_resume",
                       sprites.game_resume_button_state,
                       sprites.game_resume_button_active,
                       sprites.game_resume_button_pressed,
                       level_manager)

pause_buttons.append(button_resume)

button_restart = Button(980, 290, 150, 150,
                        "pause_restart",
                        sprites.game_restart_button_state,
                        sprites.game_restart_button_active,
                        sprites.game_restart_button_pressed,
                        level_manager)

pause_buttons.append(button_restart)

button_exit = Button(980, 460, 150, 150,
                     "pause_exit",
                     sprites.game_exit_button_state,
                     sprites.game_exit_button_active,
                     sprites.game_exit_button_pressed,
                     level_manager)

pause_buttons.append(button_exit)

pause_menu = Menu(940, 100, 220, 550, sprites.game_pause_menu_background, pause_buttons)

menus.append(pause_menu)

pause_button = Button(1180, 20, 50, 50,
                      "pause_button",
                      sprites.game_pause_button_state,
                      sprites.game_pause_button_active,
                      sprites.game_pause_button_pressed,
                      level_manager)

camera = Camera(screen, current_level.world_width, 2000)

game = Game(
    sprites.wheel_sprite,
    sprites.body_sprite,
    pause_button,
    level_manager,
    sprites,
    camera,
    labels
)

entry_menu.is_active = True
current_menu = entry_menu
clock = pg.time.Clock()
while True:
    dt = clock.tick(60) / 1000.0

    for i in menus:
        if i.is_active:
            current_menu = i

    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if game.is_active:
            game.pause_button.update(event, entry_menu, main_menu, game, pause_menu, finish_menu, fail_menu)
            current_menu = pause_menu

        if not game.is_active:
            current_menu.update(event, entry_menu, main_menu, game, pause_menu, finish_menu, fail_menu)

    if not game.is_active:
        current_menu.draw(screen)

    if game.is_active:
        game.update(dt, finish_menu, fail_menu)
        game.draw(screen)

    pg.display.flip()
