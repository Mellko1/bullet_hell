import pygame, sys


class Engine:

    activeScreen = None
    screen = None
    clock = pygame.time.Clock()
    knownScreens = None
    lastScore = 0

    def __init__(self):
        pass

    def setActiveScreen(self, _screen):
        self.activeScreen = self.knownScreens[_screen]
        self.activeScreen.onScreenAvtivation()


    def setResolution(self, _size):
        self.screen = pygame.display.set_mode(_size)

    def registerScreen(self, _name, _screen):
        if self.knownScreens is None:
            self.knownScreens = {_name: _screen}
        else:
            self.knownScreens[_name] = _screen

    def mainLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quitGame()
                else:
                    self.activeScreen.onEvent(event)

            self.activeScreen.render(self.screen)
            self.activeScreen.onTick(self.clock)

    def quitGame(self):
        sys.exit()
