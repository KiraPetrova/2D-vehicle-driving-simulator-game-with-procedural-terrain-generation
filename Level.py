class Level:

    def __init__(self,
                 name,
                 world_width,
                 frequencies,
                 amplitudes,
                 seeds,
                 ground_color,
                 gravity,
                 background_color,
                 time,
                 ground_constant,
                 ground_damping_constant):
        self.name = name
        self.world_width = world_width
        self.frequencies = frequencies
        self.amplitudes = amplitudes
        self.seeds = seeds
        self.ground_color = ground_color
        self.gravity = gravity
        self.background_color = background_color
        self.time = time
        self.ground_constant = ground_constant
        self.ground_damping_constant = ground_damping_constant

