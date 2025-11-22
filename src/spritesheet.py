import pygame

class Spritesheet:
    def __init__(self, filename):
        # Accept either a filename or an already-loaded Surface
        if isinstance(filename, pygame.Surface):
            self.spritesheet = filename.convert()
        else:
            self.spritesheet = pygame.image.load(filename).convert()

    def get_sprite(self, x, y, width, height, colorkey=None):
        sprite = pygame.Surface((width, height))
        sprite.blit(self.spritesheet, (0, 0), (x, y, width, height))
        if colorkey is not None:
            if colorkey == -1:
                colorkey = sprite.get_at((0, 0))
            sprite.set_colorkey(colorkey, pygame.RLEACCEL)
        return sprite





