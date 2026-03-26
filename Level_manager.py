from Level import *
import json
from Ground import *
import numpy as np


class Level_manager:
    def __init__(self, sprites):
        self.sprites = sprites

        self.level_1 = Level(
            name="Уровень 1",
            world_width=5000,
            frequencies=np.array([0.0007, 0.0000003, 0.00008]),
            amplitudes=np.array([2000, 1000, 2000]),
            seeds=np.array([11, 33, 22]),
            ground_color=(139, 90, 43),
            gravity=1500,
            background_color=(135, 206, 235),
            ground_constant=35000,
            ground_damping_constant=300,
            time=20
        )

        self.level_2 = Level(
            name="Уровень 2",
            world_width=5000,
            frequencies=np.array([0.0009, 0.0000003, 0.00008]),
            amplitudes=np.array([1500, 1000, 2000]),
            seeds=np.array([32, 53, 34]),
            ground_color=(85, 107, 47),
            gravity=1500,
            background_color=(47, 79, 79),
            ground_constant=35000,
            ground_damping_constant=2000,
            time=20
        )

        self.level_3 = Level(
            name="Уровень 3",
            world_width=5000,
            frequencies=np.array([0.0007, 0.000003, 0.00004]),
            amplitudes=np.array([2000, 1000, 1000]),
            seeds=np.array([9, 32, 62]),
            ground_color=(188, 143, 143),
            gravity=400,
            background_color=(0, 0, 0),
            ground_constant=50000,
            ground_damping_constant=1500,
            time=20
        )

        self.ground_1 = Ground(
            self.level_1.world_width,
            self.level_1.frequencies,
            self.level_1.amplitudes,
            self.level_1.seeds,
            self.level_1.ground_color,
            self.level_1.ground_constant,
            self.level_1.ground_damping_constant
        )

        self.ground_2 = Ground(
            self.level_2.world_width,
            self.level_2.frequencies,
            self.level_2.amplitudes,
            self.level_2.seeds,
            self.level_2.ground_color,
            self.level_2.ground_constant,
            self.level_2.ground_damping_constant
        )

        self.ground_3 = Ground(
            self.level_3.world_width,
            self.level_3.frequencies,
            self.level_3.amplitudes,
            self.level_3.seeds,
            self.level_3.ground_color,
            self.level_3.ground_constant,
            self.level_3.ground_damping_constant
        )

        self.levels = [self.level_1, self.level_2, self.level_3]
        self.grounds = [self.ground_1, self.ground_2, self.ground_3]
        self.current_level_index = 0
        self.last_unlocked_level = self.load_progress()

    def load_progress(self):
        with open("opened_levels_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("last_unlocked_level")

    def save_progress(self, new_unlocked_index):
        if new_unlocked_index >= self.last_unlocked_level:
            self.last_unlocked_level = new_unlocked_index + 1
            data = {"last_unlocked_level": self.last_unlocked_level}
            with open("opened_levels_data.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    def set_current_level_by_index(self, index: int):
        if 0 <= index < len(self.levels):
            self.current_level_index = index

    def get_current_level(self):
        return self.levels[self.current_level_index]

    def next_level(self):
        if self.current_level_index + 1 < len(self.levels):
            self.current_level_index += 1
