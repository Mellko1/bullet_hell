import pygame
from Bullet import Bullet
import random
from enum import Enum
import math

class Enemy(pygame.sprite.Sprite):
    speed = None
    img = None
    rect = None
    movMultiply = pygame.math.Vector2() # decyduje o kierunku i predkosci poruszania sie wrogow
    shootCounter = 0
    shootType = None

    def __init__(self, _imgPath, _speed, _pos, _movMultiply, _shootType):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(_imgPath)
        self.img = pygame.transform.scale(self.img, (int(0.15 * self.img.get_width()), int(0.15 * self.img.get_height())))
        self.img = pygame.transform.flip(self.img, 0, 1)
        self.rect = self.img.get_rect()
        self.rect = self.rect.move(_pos)
        self.speed = _speed
        self.movMultiply = _movMultiply
        self.shootType = _shootType

    def move(self, _gameView):
        self.rect = self.rect.move(self.speed * self.movMultiply.x, self.speed * self.movMultiply.y)


    def render(self, _surface):
        _surface.blit(self.img, self.rect)

    def shoot(self, _bulletList, _playerPos):
        self.shootCounter += 1
        if self.shootCounter == 20:
            self.shootCounter = 0

            # generuje pociski z zaleznosci od typu strzalu

            if self.shootType == ShootType.NORMAL:
                self.bulletAdd(_bulletList, 0, 1)

            elif self.shootType == ShootType.FOURDIRECTION:
                self.bulletAdd(_bulletList, 0, 1)
                self.bulletAdd(_bulletList, 1, 0)
                self.bulletAdd(_bulletList, 0, -1)
                self.bulletAdd(_bulletList, -1, 0)

            elif self.shootType == ShootType.AIMED:
                xP = _playerPos.x
                yP = _playerPos.y
                xE = self.rect.x
                yE = self.rect.y
                r = math.sqrt(pow(abs(xP - xE), 2) + pow(abs(yP - yE), 2))
                sin = (yP - yE)/r
                cos = (xP - xE)/r
                self.bulletAdd(_bulletList, cos, sin)

            elif self.shootType == ShootType.EIGHTDIRECTION:
                self.bulletAdd(_bulletList, 0, 1)
                self.bulletAdd(_bulletList, 1, 0)
                self.bulletAdd(_bulletList, -1, 0)
                self.bulletAdd(_bulletList, 0, -1)
                self.bulletAdd(_bulletList, 1, 1)
                self.bulletAdd(_bulletList, -1, 1)
                self.bulletAdd(_bulletList, 1, -1)
                self.bulletAdd(_bulletList, -1, -1)

            elif self.shootType == ShootType.DOUBLE:
                _bulletList.add(Bullet("data/new_bullet.png",
                                       pygame.math.Vector2(self.rect.left,
                                                           self.rect.top + self.img.get_height() / 2 - 3),
                                       3,
                                       pygame.math.Vector2(0, 1),
                                       8))
                _bulletList.add(Bullet("data/new_bullet.png",
                                       pygame.math.Vector2(self.rect.right,
                                                           self.rect.top + self.img.get_height() / 2 - 3),
                                       3,
                                       pygame.math.Vector2(0, 1),
                                       8))


    def bulletAdd(self, _bulletList, xDir, yDir):
        bulletRadius = 3
        _bulletList.add(Bullet("data/new_bullet.png",
                               pygame.math.Vector2(self.rect.left + self.img.get_width() / 2 - bulletRadius,
                                                   self.rect.top + self.img.get_height() / 2 - bulletRadius),
                               bulletRadius,
                               pygame.math.Vector2(xDir, yDir),
                               8))


class ShootType(Enum):
    NORMAL = 1
    FOURDIRECTION = 2
    EIGHTDIRECTION = 3
    AIMED = 4
    DOUBLE = 5
