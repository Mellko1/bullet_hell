import pygame


class Screen:

    ref_engine = None

    def __init__(self, _engine):
        self.ref_engine = _engine

    def render(self, _screen):
        pass

    def onEvent(self, _event):
        pass

    def onTick(self, _clock):
        pass

    def onScreenAvtivation(self):
        pass

    # rysuje opcje w ekranie menu i gameover
    def drawOptions(self, _options, _chosenOption):

        x = self.ref_engine.screen.get_width()
        y = self.ref_engine.screen.get_height()

        i = 0
        for option in _options:
            text = pygame.font.Font(pygame.font.get_default_font(), 20)
            color = (255, 255, 255)
            if option == _chosenOption: color = (0, 255, 0)
            surf = text.render(_options[option], 1, color)
            rect = pygame.Rect(x / 2 - surf.get_width() / 2, y / 2 + i, 0, 0)
            self.ref_engine.screen.blit(surf, rect)
            i += 40