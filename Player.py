import pygame
from Bullet import Bullet

class Player(pygame.sprite.Sprite):

    speed = 5
    img = None
    rect = None
    lives = 10
    score = 0
    multp = 1
    level = 1


    def __init__(self, _pos):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("data/Spaceship_tut.png")
        self.img = pygame.transform.scale(self.img, (int(0.2 * self.img.get_width()), int(0.2 * self.img.get_height())))
        self.rect = self.img.get_rect()
        self.rect = self.rect.move(_pos)


    def move(self, _gameView, _direction):

        rect = self.rect.move(_direction * self.speed)
        rectL = self.rect.move(0, _direction.y * self.speed)
        rectR = self.rect.move(_direction.x * self.speed, 0)

        if _gameView.rect.contains(rect):
            self.rect = rect
        elif _gameView.rect.contains(rectL):
            self.rect = rectL
        elif _gameView.rect.contains(rectR):
            self.rect = rectR

    def render(self, _surface):
        _surface.blit(self.img, self.rect)

    def shoot(self):
        bulletRadius = 2
        return Bullet("data/new_bullet.png",
                      pygame.math.Vector2(self.rect.left + self.img.get_width() / 2 - bulletRadius, self.rect.top),
                      bulletRadius,
                      pygame.math.Vector2(0, -1),
                      10)

