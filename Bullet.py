import pygame
import math

class Bullet(pygame.sprite.Sprite):

    img = None
    rect = None
    direction = None
    speed = None

    def __init__(self, _imgPath, _pos, _radius, _direction, _speed):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(_imgPath)
        self.img = pygame.transform.scale(self.img, (2 * _radius, 2 * _radius))
        self.rect = self.img.get_rect()
        self.rect = self.rect.move(_pos)
        self.direction = _direction
        self.speed = _speed


    def render(self, _surface):
        _surface.blit(self.img, self.rect)

    def move(self, _gameView):
        self.rect = self.rect.move(math.ceil(self.direction.x * self.speed), math.ceil(self.direction.y * self.speed))
        if not _gameView.rect.contains(self.rect):
            del self
            return True


