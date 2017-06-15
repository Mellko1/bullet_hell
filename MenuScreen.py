import pygame
from Screen import Screen


class MenuScreen(Screen):

    chosenOption = 0
    chosenOption = 0
    opcje = {
        0: "New Game",
        1: "Quit"
    }

    def __init__(self, _engine):
        super(MenuScreen, self).__init__(_engine)

    def render(self, _screen):
        _screen.fill((0, 0, 0))

        text = pygame.font.Font(pygame.font.get_default_font(), 40)
        surf = text.render("Main Menu", 1, (255, 255, 255))

        x = _screen.get_width()
        y = _screen.get_height()

        rect = pygame.Rect(x / 2 - surf.get_width() / 2, y / 2 - 100, 0, 0)
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
                if self.opcje[self.chosenOption] == "New Game":
                    self.ref_engine.setActiveScreen("Gameplay")
                elif self.opcje[self.chosenOption] == "Quit":
                    self.ref_engine.quitGame()