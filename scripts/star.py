import pygame 

class Star:
    def __init__(self, game, pos):
        self.game = game
        self.pos = list(pos)
        self.animation = game.assets['star']

    def update(self):
        self.animation.update()

    def render(self, surface, offset):
        img = self.animation.img()
        surface.blit(img, (self.pos[0] - img.get_width() / 2 - offset[0], self.pos[1] - img.get_height() / 2 - offset[1]))

    def rect(self):
        img = self.animation.img()
        return pygame.Rect(self.pos[0] - img.get_width() / 2, self.pos[1] - img.get_height() / 2, img.get_width(), img.get_height())
