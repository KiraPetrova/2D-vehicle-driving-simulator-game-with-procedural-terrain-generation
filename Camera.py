class Camera:
    def __init__(self, screen, world_width, world_height):
        self.x = 0
        self.y = 0
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.world_width = world_width
        self.world_height = world_height

    def update_world_width(self, new_width):
        self.world_width = new_width

    def current(self, body):
        self.x = body.x - self.screen_width // 2
        if self.x < 0:
            self.x = 0
        if self.x > self.world_width - self.screen_width:
            self.x = self.world_width - self.screen_width

        self.y = body.y - self.screen_height // 2
        if self.y < 0:
            self.y = 0
        if self.y > self.world_height - self.screen_height:
            self.y = self.world_height - self.screen_height
