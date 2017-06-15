import pygame
from View import View


class ScoreView(View):
    def __init__(self, _surface, _rekt, _player, _engine):
        super(ScoreView, self).__init__(_surface, _rekt, _player, _engine)

    def render(self):

        # renderowanie zyc

        img = pygame.image.load("data/heart.png")
        img = pygame.transform.scale(img, (int(0.5 * img.get_width()), int(0.5 * img.get_height())))
        rect = img.get_rect()
        rect = rect.move((self.rect.x + 5, self.rect.y + 5))

        for i in range(self.player.lives):
            self.surface.blit(img, rect)
            rect = rect.move((20, 0))
            if rect.right > self.rect.right:
                rect = rect.move((-self.rect.width + 5, 20))

        # renderowanie tekstow

        text = pygame.font.Font(pygame.font.get_default_font(), 18)
        surf = text.render("Score: " + str(self.player.score), 1, (255, 255, 255))
        rect = pygame.Rect(self.rect.left + 10, self.rect.bottom - 10 - surf.get_rect().height , 0, 0)
        self.ref_engine.screen.blit(surf, rect)

        surf = text.render("Combo: " + str(self.player.multp - 1), 1, (255, 255, 255))
        rect = pygame.Rect(self.rect.left + 10, self.rect.bottom - 30 - surf.get_rect().height, 0, 0)
        self.ref_engine.screen.blit(surf, rect)

        surf = text.render("Level: " + str(self.player.level), 1, (255, 255, 255))
        rect = pygame.Rect(self.rect.left + 10, self.rect.bottom - 50 - surf.get_rect().height, 0, 0)
        self.ref_engine.screen.blit(surf, rect)

        surf = text.render("move - arrow keys", 1, (255, 255, 255))
        rect = pygame.Rect(self.rect.left + 10, self.rect.bottom - 120 - surf.get_rect().height, 0, 0)
        self.ref_engine.screen.blit(surf, rect)

        surf = text.render("shoot - Z", 1, (255, 255, 255))
        rect = pygame.Rect(self.rect.left + 10, self.rect.bottom - 100 - surf.get_rect().height, 0, 0)
        self.ref_engine.screen.blit(surf, rect)

        super(ScoreView, self).render()
