import pygame


class View(pygame.sprite.Sprite):

    ref_engine = None
    player = None
    rect = None
    surface = None
    activeLevel = None

    def __init__(self, _surface, _rekt, _player, _engine):
        pygame.sprite.Sprite.__init__(self)
        self.player = _player
        self.rect = _rekt
        self.surface = _surface
        self.ref_engine = _engine

    def render(self):
        pygame.draw.rect(self.surface, (255, 255, 255), self.rect, 1)
