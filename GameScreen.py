import pygame
from Screen import Screen
from Player import Player
from GameView import GameView
from ScoreView import ScoreView




class GameScreen(Screen):

    player = Player((400, 400))

    gameView = None
    scoreView = None

    def __init__(self, _engine):
        super(GameScreen, self).__init__(_engine)
        self.setViews()

    def onScreenAvtivation(self):
        self.newGame()

    def newGame(self):
        self.player.rect.move_ip(400 - self.player.rect.x, 400 - self.player.rect.y)
        self.player.lives = 10
        self.player.score = 0
        self.player.level = 1
        self.gameView.newGame()

    # ustawia oddzielne widoki na ekranie gry (widok rozgrywki i informacji dodatkowych)
    def setViews(self):
        width = self.ref_engine.screen.get_width()
        height = self.ref_engine.screen.get_height()

        self.gameView = GameView(self.ref_engine.screen, pygame.Rect(10, 10, width * 3 / 4 - 15, height - 20), self.player, self.ref_engine)
        self.scoreView = ScoreView(self.ref_engine.screen, pygame.Rect(width * 3 / 4 + 5, 10, width / 4 - 15, height - 20), self.player, self.ref_engine)

    def render(self, _screen):
        _screen.fill((0, 0, 0))
        self.gameView.render()
        self.renderBlackBars(_screen)
        self.scoreView.render()
        pygame.display.flip()

    def onEvent(self, _event):
        self.gameView.onEvent(_event)


    def onTick(self, _clock):
        super(GameScreen, self).onTick(_clock)
        self.gameView.onTick(_clock)



    # renderuje czarne prostokaty na okolo widoku rozgrywki, aby przeciwnicy mogli sie za nimi "chowac"
    def renderBlackBars(self, _screen):
        screenWidth = _screen.get_width()
        screenHeight = _screen.get_height()
        viewWidth = self.gameView.rect.width
        viewHeight = self.gameView.rect.height
        viewX = self.gameView.rect.x
        viewY = self.gameView.rect.y

        rectL = pygame.Rect(0, 0, viewX, _screen.get_height())
        rectR = pygame.Rect(viewX + viewWidth, 0, screenWidth - viewX - viewWidth, screenHeight)
        rectU = (0, 0, screenWidth, viewY)
        rectD = (0, viewY + viewHeight, screenWidth, screenHeight - viewY - viewHeight)

        pygame.draw.rect(_screen, (0, 0, 0), rectL)
        pygame.draw.rect(_screen, (0, 0, 0), rectR)
        pygame.draw.rect(_screen, (0, 0, 0), rectU)
        pygame.draw.rect(_screen, (0, 0, 0), rectD)
