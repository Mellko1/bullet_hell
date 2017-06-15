import pygame
from Screen import Screen

class GameoverScreen(Screen):

    chosenOption = 0
    opcje = {
        0: "Try Again",
        1: "Main Menu"
    }

    def __init__(self, _engine):
        super(GameoverScreen, self).__init__(_engine)

    def render(self, _screen):
        _screen.fill((0, 0, 0))

        text = pygame.font.Font(pygame.font.get_default_font(), 40)
        surf = text.render("Game Over", 1, (255, 255, 255))

        x = _screen.get_width()
        y = _screen.get_height()

        rect = pygame.Rect(x / 2 - surf.get_width() / 2, y / 2 - 100, 0, 0)
        _screen.blit(surf, rect)

        text = pygame.font.Font(pygame.font.get_default_font(), 18)
        surf = text.render("Score: " + str(self.ref_engine.lastScore), 1, (255, 255, 255))
        rect = pygame.Rect(x / 2 - surf.get_width() / 2, y / 2 - 50, 0, 0)
        _screen.blit(surf, rect)

        self.drawOptions(self.opcje, self.chosenOption)

        pygame.display.flip()

    def onEvent(self, _event):
        if _event.type == pygame.KEYDOWN:
            if _event.key == pygame.K_DOWN:
                self.chosenOption = (self.chosenOption + 1) % len(self.opcje)
            elif _event.key == pygame.K_UP:
                self.chosenOption  = (self.chosenOption - 1) % len(self.opcje)
            elif _event.key == pygame.K_RETURN:
                if self.opcje[self.chosenOption] == "Try Again":
                    self.ref_engine.setActiveScreen("Gameplay")
                elif self.opcje[self.chosenOption] == "Main Menu":
                    self.ref_engine.setActiveScreen("Menu")

    def onTick(self, _clock):
        pass